import aws_cdk as cdk
import os.path
from cdk_ec2_key_pair import KeyPair
from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_iam as iam,
    aws_s3 as s3,
    aws_backup as bk,
    aws_events as event,
    aws_s3_deployment as s3deploy,
    aws_s3_assets as s3assets
)
from constructs import Construct

dirname = os.path.dirname(__file__)

with open("./hello_cdk/user_data/user-data.sh") as f:
    user_data = f.read()


class CdkVpcStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        bucket = s3.Bucket(
            self, "Bucket",
            versioned=True,
            removal_policy=cdk.RemovalPolicy.DESTROY,
            encryption=s3.BucketEncryption.KMS_MANAGED,
            auto_delete_objects=True
        )

        s3deploy.BucketDeployment(
            self, "S3Deployment",
            sources=[s3deploy.Source.asset("./hello_cdk/user_data")],
            destination_bucket=bucket,
        )

        vpc1 = ec2.Vpc(
            self, "VPC1",
            max_azs=2,
            cidr="10.10.10.0/24",
            # configuration will create 2 groups in 2 AZs = 4 subnets.
            subnet_configuration=[ec2.SubnetConfiguration(
                subnet_type=ec2.SubnetType.PUBLIC,
                name="Public1",
                cidr_mask=25
            )
            ]
        )

        vpc2 = ec2.Vpc(
            self, "VPC2",
            max_azs=2,
            cidr="10.20.20.0/24",
            subnet_configuration=[ec2.SubnetConfiguration(
                subnet_type=ec2.SubnetType.PUBLIC,
                name="Public2",
                cidr_mask=25
            )
            ]
        )
        #  CfnOutput(self, "Output", value=self.vpc.vpc_id)

        self.cfn_vPCPeering_connection = ec2.CfnVPCPeeringConnection(
            self, "MyCfnVPCPeeringConnection",
            peer_vpc_id=vpc1.vpc_id,
            vpc_id=vpc2.vpc_id,

            # the properties below are optional
            peer_region="eu-central-1",
        )

        amzn_linux = ec2.MachineImage.latest_amazon_linux(
            generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2,
            edition=ec2.AmazonLinuxEdition.STANDARD,
            virtualization=ec2.AmazonLinuxVirt.HVM,
            storage=ec2.AmazonLinuxStorage.GENERAL_PURPOSE,
        )

        windows = ec2.MachineImage.latest_windows(ec2.WindowsVersion.WINDOWS_SERVER_2019_ENGLISH_FULL_BASE)

        role = iam.Role(self, "InstanceSSM", assumed_by=iam.ServicePrincipal("ec2.amazonaws.com"))

        role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name("AmazonSSMManagedInstanceCore"))

        Management_sg = ec2.SecurityGroup(
            self, "Management SecurityGroup",
            vpc=vpc2,
            description="Allow ssh & RDP access to ec2 instances",
            allow_all_outbound=True
        )

        Management_sg.add_ingress_rule(ec2.Peer.any_ipv4(), ec2.Port.tcp(22), "allow ssh access from the world")
        Management_sg.add_ingress_rule(ec2.Peer.any_ipv4(), ec2.Port.tcp(3389), "allow RDP access from the world")

        Webserver_sg = ec2.SecurityGroup(
            self, "Webserver SecurityGroup",
            vpc=vpc1,
            description="Allow http & https access to ec2 instances",
            allow_all_outbound=True
        )
        Webserver_sg.add_ingress_rule(ec2.Peer.any_ipv4(), ec2.Port.tcp(80), "allow http access from the world")
        Webserver_sg.add_ingress_rule(ec2.Peer.any_ipv4(), ec2.Port.tcp(443), "allow https access from the world")

        # Create a key pair with lambda function that will store the public and private key in secrets manager

        key = KeyPair(
            self, "KeyPair",
            name="MyKeyPair",
            description="MyKeyPair",
            store_public_key=True)

        key.grant_read_on_private_key(role)
        key.grant_read_on_public_key(role)

        asset = s3assets.Asset(self, "Asset", path="./hello_cdk/user_data/user-data.sh")

        Webserver = ec2.Instance(
            self, "Webserver",
            instance_type=ec2.InstanceType("t2.micro"),
            machine_image=amzn_linux,
            security_group=Webserver_sg,
            vpc=vpc1,
            role=role,
            availability_zone="eu-central-1a",
            block_devices=[ec2.BlockDevice(
                device_name="/dev/xvda",
                volume=ec2.BlockDeviceVolume.ebs(8,
                                                 encrypted=True
                                                 )
            )
            ]
        )

        local_path = Webserver.user_data.add_s3_download_command(
            bucket=asset.bucket,
            bucket_key=asset.s3_object_key,
            region="eu-central-1"
        )

        Webserver.user_data.add_execute_file_command(file_path=local_path, arguments="--verbose -y")

        asset.grant_read(Webserver.role)

        ManagementServer = ec2.Instance(
            self, "ManagementServer",
            instance_type=ec2.InstanceType("t2.micro"),
            machine_image=windows,
            vpc=vpc2,
            security_group=Management_sg,
            role=role,
            availability_zone="eu-central-1b",
            key_name=key.key_pair_name,
            block_devices=[ec2.BlockDevice(
                device_name="/dev/sda1",
                volume=ec2.BlockDeviceVolume.ebs(30,
                                                 encrypted=True
                                                 )
            )
            ]
        )

        backup_plan = bk.BackupPlan(
            self, "UsStorageBackupPlanEBS",
            backup_plan_name="us-storage-ebs-volume"
        )

        backup_vault_name = "us-storage-ebs-volume"
        bk_vault = bk.BackupVault(
            self, "us-storage-ebs-volume",
            backup_vault_name=backup_vault_name,
            removal_policy=cdk.RemovalPolicy.DESTROY
        )

        backup_plan.add_rule(
            rule=bk.BackupPlanRule(
                backup_vault=bk_vault,
                rule_name='backup-ebs-volume-daily',
                delete_after=cdk.Duration.days(7),
                schedule_expression=event.Schedule.cron(
                    minute="0",
                    hour="0",
                    month="*",
                    week_day="*",
                    year="*"
                )
            )
        )

        backup_plan.add_selection(
            "us-storage-ebs-volume",
            backup_selection_name="BackupSelection",
            resources=[
                bk.BackupResource.from_ec2_instance(ManagementServer),
                bk.BackupResource.from_ec2_instance(Webserver)
            ]
        )
