import aws_cdk.aws_elasticloadbalancingv2 as elbv2
from aws_cdk.aws_elasticloadbalancingv2 import SslPolicy
import aws_acm_certified as acm
import aws_cdk as cdk
from cdk_ec2_key_pair import KeyPair
from aws_cdk.aws_s3_assets import Asset
from aws_cdk import (
    Tags,
    Stack,
    aws_ec2 as ec2,
    aws_s3 as s3,
    aws_backup as bk,
    aws_events as event,
    aws_s3_deployment as s3deploy,
    aws_autoscaling as autoscaling,
)
from constructs import Construct


class HelloCdkStack(Stack):

    def __init__(self, scope: Construct, id: str, env) -> None:
        super().__init__(scope, id, env=env)

        # Parameters variables.

        environments = self.node.try_get_context("ENVIRONMENTS")
        Bucket_environment = environments.get("bucket")
        bucket_name = Bucket_environment.get("bucket_name")
        versioned = Bucket_environment.get("versioned")
        auto_delete_objects = Bucket_environment.get("auto_delete_objects")

        s3deploy_environment = environments.get("s3deploy")
        s3Deployment_name = s3deploy_environment.get("name")
        sources = s3deploy_environment.get("sources")

        vpc_environment = environments.get("managementserver_vpc")
        vpc_name = vpc_environment.get("name")
        max_azs = vpc_environment.get("max_az")
        cidr = vpc_environment.get("cidr")
        subnet_name = vpc_environment.get("subnet_name")
        cidr_mask = vpc_environment.get("cidr_mask")

        second_vpc_environment = environments.get("webserver_vpc")
        second_vpc_name = second_vpc_environment.get("name")
        second_max_azs = second_vpc_environment.get("max_az")
        second_cidr = second_vpc_environment.get("cidr")
        second_subnet_name = second_vpc_environment.get("subnet_name")
        second_cidr_mask = second_vpc_environment.get("cidr_mask")
        private_subnet_name = second_vpc_environment.get("private_subnet_name")
        private_cidr_mask = second_vpc_environment.get("cidr_mask_private")

        peering_environment = environments.get("peering")
        peering_name = peering_environment.get("name")
        peer_region = peering_environment.get("peer_region")

        route_environment = environments.get("route")
        route_name = route_environment.get("name")

        second_route_environment = environments.get("second_route")
        second_route_name = second_route_environment.get("name")

        mm_sg_environment = environments.get("management_security_group")
        mm_sg_name = mm_sg_environment.get("name")
        mm_sg_description = mm_sg_environment.get("description")
        mm_sg_ob = mm_sg_environment.get("allow_all_outbound")

        allowed_ipv4 = mm_sg_environment.get("allowed_ipv4")
        mm_sg_ssh_port = mm_sg_environment.get("ssh_allowed_port")
        mm_sg_ing_ssh_desc = mm_sg_environment.get("ssh_port_description")
        mm_sg_rdp_port = mm_sg_environment.get("rdp_allowed_port")
        mm_sg_rdp_ssh_desc = mm_sg_environment.get("rdp_port_description")

        wb_sg_environment = environments.get("webserver_security_group")
        wb_sg_name = wb_sg_environment.get("name")
        wb_sg_description = wb_sg_environment.get("description")
        wb_sg_ob = wb_sg_environment.get("allow_all_outbound")

        wb_sg_ssh_port = wb_sg_environment.get("ssh_allowed_port")
        wb_sg_ssh_desc = wb_sg_environment.get("ssh_port_description")

        mm_key_env = environments.get('management_key_pair')
        mm_key_name = mm_key_env.get('name')
        mm_key_desc = mm_key_env.get('description')
        mm_key_store = mm_key_env.get('store_public_key')

        web_key_env = environments.get('webserver_key_pair')
        web_key_name = web_key_env.get('name')
        web_key_desc = web_key_env.get('description')
        web_key_store = web_key_env.get('store_public_key')

        web_instance_environment = environments.get("webserver_instance")
        web_instance_name = web_instance_environment.get("name")
        web_instance_type = web_instance_environment.get("instance_type")
        web_instance_root = web_instance_environment.get("root_device_directory")
        web_instance_size = web_instance_environment.get("volume_size")
        web_instance_encrypt = web_instance_environment.get("encrypted_volume")
        web_instance_asset = web_instance_environment.get("asset_bucket")
        web_instance_path = web_instance_environment.get("asset_path")
        web_instance_region = web_instance_environment.get("asset_region")

        lb_environment = environments.get("LoadBalancer")
        lb_name = lb_environment.get("name")
        lb_internet_facing = lb_environment.get("internet_facing")
        lb_listeners_name = lb_environment.get("listener_name")
        lb_listeners_port = lb_environment.get("listener_port")
        lb_redirect_source_port = lb_environment.get("redirect_source_port")
        lb_redirect_target_port = lb_environment.get("redirect_target_port")
        lb_target_name = lb_environment.get("target_name")
        lb_target_port = lb_environment.get("target_port")
        lb_cpu_utilization_name = lb_environment.get("cpu_utilization_name")
        lb_target_utilization_percent = lb_environment.get("target_utilization_percent")

        web_tags_environment = environments.get("webserver_tags")
        web_tag_key = web_tags_environment.get("tag_key")
        web_tag_value = web_tags_environment.get("tag_value")

        mm_instance_environment = environments.get("managementserver_instance")
        mm_instance_name = mm_instance_environment.get("name")
        mm_instance_type = mm_instance_environment.get("instance_type")
        mm_instance_avz = mm_instance_environment.get("availability_zone")
        mm_instance_root = mm_instance_environment.get("root_device_directory")
        mm_instance_size = mm_instance_environment.get("volume_size")
        mm_instance_encrypt = mm_instance_environment.get("encrypted_volume")

        web_bk_environment = environments.get("webserver_backup")
        web_bk_backup = web_bk_environment.get("name")
        web_bk_name = web_bk_environment.get("backup_plan_name")
        web_bk_vault = web_bk_environment.get("backup_vault_name")
        web_bk_rule = web_bk_environment.get("backup_rule_name")
        web_bk_del = web_bk_environment.get("delete_backup_after_days")
        web_bk_min = web_bk_environment.get("cron_minute")
        web_bk_hour = web_bk_environment.get("cron_hour")
        web_bk_month = web_bk_environment.get("cron_month")
        web_bk_week = web_bk_environment.get("cron_week_day")
        web_bk_select = web_bk_environment.get("backup_selection_name")

        man_bk_environment = environments.get("managementserver_backup")
        man_bk_backup = man_bk_environment.get("name")
        man_bk_name = man_bk_environment.get("backup_plan_name")
        man_bk_vault = man_bk_environment.get("backup_vault_name")
        man_bk_rule = man_bk_environment.get("backup_rule_name")
        man_bk_del = man_bk_environment.get("delete_backup_after_days")
        man_bk_min = man_bk_environment.get("cron_minute")
        man_bk_hour = man_bk_environment.get("cron_hour")
        man_bk_month = man_bk_environment.get("cron_month")
        man_bk_week = man_bk_environment.get("cron_week_day")
        man_bk_select = man_bk_environment.get("backup_selection_name")

        # S3 Bucket creation.

        bucket = s3.Bucket(
            self,
            bucket_name,
            versioned=versioned,
            removal_policy=cdk.RemovalPolicy.DESTROY,
            encryption=s3.BucketEncryption.KMS_MANAGED,
            auto_delete_objects=auto_delete_objects
        )

        # S3 Bucket file deployment.

        s3deploy.BucketDeployment(
            self, s3Deployment_name,
            sources=[s3deploy.Source.asset(sources)],
            destination_bucket=bucket
        )

        # vpc creation for webserver, includes 2 public subnets and 2 az.

        vpc1 = ec2.Vpc(
            self, second_vpc_name,
            max_azs=second_max_azs,
            cidr=second_cidr,
            subnet_configuration=[ec2.SubnetConfiguration(
                subnet_type=ec2.SubnetType.PUBLIC,
                name=second_subnet_name,
                cidr_mask=second_cidr_mask
            ),
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PRIVATE_WITH_NAT,
                    name=private_subnet_name,
                    cidr_mask=private_cidr_mask
                )
            ]
        )

        # vpc creation for management server, includes 2 public subnets and 2 az.

        vpc2 = ec2.Vpc(
            self, vpc_name,
            max_azs=max_azs,
            cidr=cidr,
            # configuration will create 2 groups in 2 AZs = 4 subnets.
            subnet_configuration=[ec2.SubnetConfiguration(
                subnet_type=ec2.SubnetType.PUBLIC,
                name=subnet_name,
                cidr_mask=cidr_mask
            )
            ]
        )
        #
        # # Deployment of vpc-peering.
        #
        Peering_connection = ec2.CfnVPCPeeringConnection(
            self, peering_name,
            peer_vpc_id=vpc1.vpc_id,
            vpc_id=vpc2.vpc_id,

            # the properties below are optional
            peer_region=peer_region,
        )
        #

        for i in range(0, 1):
            ec2.CfnRoute(
                self, route_name,
                route_table_id=vpc1.public_subnets[i].route_table.route_table_id,
                destination_cidr_block=vpc2.vpc_cidr_block,
                vpc_peering_connection_id=Peering_connection.ref
            )

        for i in range(0, 1):
            ec2.CfnRoute(
                self, second_route_name,
                route_table_id=vpc2.public_subnets[i].route_table.route_table_id,
                destination_cidr_block=vpc1.vpc_cidr_block,
                vpc_peering_connection_id=Peering_connection.ref
            )

        # Linux AMI creation.

        amzn_linux = ec2.MachineImage.latest_amazon_linux(
            generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2,
            edition=ec2.AmazonLinuxEdition.STANDARD,
            virtualization=ec2.AmazonLinuxVirt.HVM,
            storage=ec2.AmazonLinuxStorage.GENERAL_PURPOSE,
        )

        # Windows AMI creation.

        windows = ec2.MachineImage.latest_windows(ec2.WindowsVersion.WINDOWS_SERVER_2019_ENGLISH_FULL_BASE)

        # Security group creation for management server.

        Management_sg = ec2.SecurityGroup(
            self, mm_sg_name,
            vpc=vpc2,
            description=mm_sg_description,
            allow_all_outbound=mm_sg_ob
        )

        allowed_ips = allowed_ipv4
        for i in range(len(allowed_ips)):
            Management_sg.add_ingress_rule(ec2.Peer.ipv4(allowed_ips[i] + "/32"), ec2.Port.tcp(mm_sg_ssh_port),
                                           mm_sg_ing_ssh_desc)

        for i in range(len(allowed_ips)):
            Management_sg.add_ingress_rule(ec2.Peer.ipv4(allowed_ips[i] + "/32"), ec2.Port.tcp(mm_sg_rdp_port),
                                           mm_sg_rdp_ssh_desc)

        # Security group creation for webserver.

        Webserver_sg = ec2.SecurityGroup(
            self, wb_sg_name,
            vpc=vpc1,
            description=wb_sg_description,
            allow_all_outbound=wb_sg_ob
        )
        #

        Webserver_sg.add_ingress_rule(ec2.Peer.security_group_id(Management_sg.security_group_id),
                                      ec2.Port.tcp(wb_sg_ssh_port), wb_sg_ssh_desc)

        # Create a key pair with lambda function that will store the public and private key in secrets manager

        # Create a key pair for the management server.

        mmkey = KeyPair(
            self, mm_key_name,
            name=mm_key_name,
            description=mm_key_desc,
            store_public_key=mm_key_store)
        #

        # Create a key pair for the webserver.

        webkey = KeyPair(
            self, web_key_name,
            name=web_key_name,
            description=web_key_desc,
            store_public_key=web_key_store)

        # ec2 instance creation for the webserver.

        asg = autoscaling.AutoScalingGroup(
            self, web_instance_name,
            instance_type=ec2.InstanceType(web_instance_type),
            machine_image=amzn_linux,
            security_group=Webserver_sg,
            vpc=vpc1,
            key_name=webkey.key_pair_name,
            block_devices=[autoscaling.BlockDevice(
                device_name=web_instance_root,
                volume=autoscaling.BlockDeviceVolume.ebs(web_instance_size,
                                                         encrypted=web_instance_encrypt
                                                         )
            )
            ],
            health_check=autoscaling.HealthCheck.ec2(
                grace=cdk.Duration.minutes(2),
            ),
            desired_capacity=1,
            min_capacity=1,
            max_capacity=3,
        )

        webkey.grant_read_on_private_key(asg.role)
        webkey.grant_read_on_public_key(asg.role)

        # Add userdata to the webserver.

        assets = Asset(self, web_instance_asset,
                       path=web_instance_path
                       )

        Local_path = asg.user_data.add_s3_download_command(
            bucket=assets.bucket,
            bucket_key=assets.s3_object_key,
            region=web_instance_region,
        )

        asg.user_data.add_execute_file_command(
            file_path=Local_path
        )

        assets.grant_read(asg.role)

        lb = elbv2.ApplicationLoadBalancer(
            self, lb_name,
            vpc=vpc1,
            internet_facing=lb_internet_facing)

        listener_certificate = elbv2.ListenerCertificate.from_arn(acm.generated_certificate())

        listener = lb.add_listener(
            lb_listeners_name,
            port=lb_listeners_port,
            certificates=[listener_certificate],
            ssl_policy=SslPolicy.RECOMMENDED
        )

        lb.add_redirect(
            source_port=lb_redirect_source_port,
            target_port=lb_redirect_target_port
        )

        listener.add_targets(
            lb_target_name,
            port=lb_target_port,
            targets=[asg]
        )
        listener.connections.allow_default_port_from_any_ipv4("Open to the world")

        asg.scale_on_cpu_utilization(
            lb_cpu_utilization_name,
            target_utilization_percent=lb_target_utilization_percent
        )

        # ec2 instance creation for the management server.

        ManagementServer = ec2.Instance(
            self, mm_instance_name,
            instance_type=ec2.InstanceType(mm_instance_type),
            machine_image=windows,
            vpc=vpc2,
            security_group=Management_sg,
            availability_zone=mm_instance_avz,
            key_name=mmkey.key_pair_name,
            block_devices=[ec2.BlockDevice(
                device_name=mm_instance_root,
                volume=ec2.BlockDeviceVolume.ebs(mm_instance_size,
                                                 encrypted=mm_instance_encrypt
                                                 )
            )
            ]
        )

        mmkey.grant_read_on_private_key(ManagementServer.role)
        mmkey.grant_read_on_public_key(ManagementServer.role)

        # Tag creation for the webserver.

        Tags.of(asg).add(web_tag_key, web_tag_value)

        # Webserver backup creation.

        web_backup_plan = bk.BackupPlan(
            self, web_bk_backup,
            backup_plan_name=web_bk_name
        )

        backup_vault_name = web_bk_vault
        bk_vault = bk.BackupVault(
            self, web_bk_vault,
            backup_vault_name=backup_vault_name,
            removal_policy=cdk.RemovalPolicy.DESTROY
        )

        web_backup_plan.add_rule(
            rule=bk.BackupPlanRule(
                backup_vault=bk_vault,
                rule_name=web_bk_rule,
                delete_after=cdk.Duration.days(web_bk_del),
                schedule_expression=event.Schedule.cron(
                    minute=web_bk_min,
                    hour=web_bk_hour,
                    month=web_bk_month,
                    week_day=web_bk_week
                )
            )
        )

        web_backup_plan.add_selection(
            web_bk_name,
            backup_selection_name=web_bk_select,
            resources=[
                bk.BackupResource.from_tag(
                    web_tag_key,
                    web_tag_value
                )
            ]
        )

        # Management server backup creation.

        man_backup_plan = bk.BackupPlan(
            self, man_bk_backup,
            backup_plan_name=man_bk_name
        )

        backup_vault_name = man_bk_vault
        second_bk_vault = bk.BackupVault(
            self, man_bk_vault,
            backup_vault_name=backup_vault_name,
            removal_policy=cdk.RemovalPolicy.DESTROY
        )

        man_backup_plan.add_rule(
            rule=bk.BackupPlanRule(
                backup_vault=second_bk_vault,
                rule_name=man_bk_rule,
                delete_after=cdk.Duration.days(man_bk_del),
                schedule_expression=event.Schedule.cron(
                    minute=man_bk_min,
                    hour=man_bk_hour,
                    month=man_bk_month,
                    week_day=man_bk_week
                )
            )
        )

        man_backup_plan.add_selection(
            man_bk_name,
            backup_selection_name=man_bk_select,
            resources=[
                bk.BackupResource.from_ec2_instance(ManagementServer)
            ]
        )
