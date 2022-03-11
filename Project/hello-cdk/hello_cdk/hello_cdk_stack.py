import aws_cdk.aws_elasticloadbalancingv2 as elbv2
from aws_cdk.aws_elasticloadbalancingv2 import SslPolicy
from aws_cdk.aws_certificatemanager import Certificate
import aws_cdk.aws_elasticloadbalancingv2_targets as targets
import aws_cdk as cdk
from cdk_ec2_key_pair import KeyPair
from aws_cdk.aws_s3_assets import Asset
from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_iam as iam,
    aws_s3 as s3,
    aws_backup as bk,
    aws_events as event,
    aws_s3_deployment as s3deploy,
    aws_autoscaling as autoscaling,
)
from constructs import Construct


# ____________¶¶
# ___________¶¶¶¶
# __________¶¶¶¶¶¶
# _________¶¶¥¥¥¶¶¶
# ________¶¶¥¥¥¥¥¶¶¶__________________________________________¶¶¶¶¶¶¶¶
# ________¶¶¥¥¥¥¥¥¶¶¶_____________________________________¶¶¶¶¶¥¥¥¥¥¶¶
# ________¶¶¥¥¥¥¥¥ƒƒ¶¶________________________________¶¶¶¶¥¥¥¥¥¥¥¥¶¶¶¶
# ________¶¶¥¥¥¥ƒƒƒƒƒ¶¶___________________________¶¶¶¶ƒƒ¥¥¥¥¥¥¥¥¶¶¶¶
# ________¶¶¶ƒƒƒƒƒƒƒƒ§¶¶________________________¶¶ƒƒƒƒƒƒƒ¥¥¥¥¥¶¶¶¶
# _________¶¶¶ƒƒƒƒƒƒ§§¶¶____________________¶¶¶¶ƒƒƒƒƒƒƒƒƒƒ¥¥¶¶¶¶
# ___________¶¶ƒƒƒƒƒ§§¶¶__________________¶¶ƒƒƒƒƒƒƒƒƒƒƒƒƒƒ¶¶¶¶
# ____________¶¶ƒƒ§§§§¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ƒƒƒƒƒƒƒƒƒƒƒƒƒƒ§§¶¶
# _____________¶¶§§§§§§§ƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒ§§§§¶¶
# ______________¶¶§§§ƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒ§§§§§¶¶¶¶___________________¶¶¶¶¶¶
# ____________¶¶ƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒ§§§¶¶¶____________________¶¶¶ƒƒƒƒƒ¶¶
# __________¶¶ƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒ¶¶¶¶¶¶ƒƒƒƒ§§§¶¶¶___________________¶¶ƒƒƒƒƒƒƒƒ¶¶
# _________¶¶ƒƒ¶¶¶¶¶ƒƒƒƒƒƒƒƒƒƒƒƒƒƒ¶¶__¶¶¶¶ƒƒƒ§§§§§¶¶________________¶¶ƒƒƒƒƒƒƒƒƒƒ¶¶
# ________¶¶ƒƒ¶¶__¶¶ƒƒƒƒƒƒƒƒƒƒƒƒƒƒ¶¶¶¶¶¶¶¶ƒƒƒ§§§§§§¶¶___________¶¶¶¶ƒƒƒƒƒƒƒƒ§§§§§§¶¶
# _______¶¶ƒƒƒ¶¶¶¶¶¶ƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒ¶¶¶¶¶¶ƒƒƒƒƒ§§§§§§¶¶________¶¶ƒƒƒƒƒƒƒƒ§§§§§§§§§§¶¶
# _______¶¶ƒƒƒƒ¶¶¶¶ƒƒƒƒƒ¥¥¥ƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒ####§§§§§¶¶____¶¶¶¶ƒƒƒƒƒƒƒƒ§§§§§§§§§§§§¶¶
# _______¶¶###ƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒ¥¥ƒƒƒƒƒƒ########§§§§¶¶¶¶¶¶ƒƒƒƒƒƒƒƒ§§§§§§§§§§§§§§§§¶¶
# _______¶¶####ƒƒƒƒƒƒƒƒ¥¥¥¥¥¥¥¥¥¥¥ƒƒƒƒƒƒ########§§¶¶¶¶ƒƒ¶¶¶¶ƒƒƒƒ§§§§§§§§§§§§§§§§§§¶¶
# ____¶¶¶¶¶¶###ƒƒƒƒƒƒƒƒƒ¥¥¥#####¥ƒƒƒƒƒƒƒ########¶¶ƒƒ¶¶ƒƒƒƒƒƒ¶¶§§§§§§§§§§§§§§§§§§§§¶¶
# __¶¶¶ƒƒ¶¶¶¶#ƒƒƒƒƒƒƒƒƒƒ¥¥####¥¥ƒƒƒƒƒƒƒƒƒƒ####§§¶¶ƒƒƒƒƒƒƒƒ¶¶¶¶§§§§§§§§§§§§§§§§¶¶¶¶
# _¶¶ƒƒ¶ƒƒƒƒ¶¶ƒƒƒƒƒƒƒƒƒƒƒƒ¥¥¥¥ƒƒƒƒƒƒƒƒƒƒƒƒƒƒ§§¶¶ƒƒƒƒƒƒƒƒƒƒƒƒ¶¶§§§§§§§§§§§§¶¶¶¶
# ¶¶ƒƒƒƒƒƒ§§§§¶¶ƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒ¶¶ƒƒƒƒƒƒƒƒ§§§§¶¶§§§§§§§§§§¶¶¶¶
# __¶¶ƒƒ§§§§§§¶¶¶¶ƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒ§§§§§¶¶¶§§§§§§§§¶¶
# ____¶¶§§§§§§§¶¶ƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒ§§§§§§¶__¶§§§§§§¶¶
# ______¶¶§§§§§§ƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒ§§§§§§¶¶____¶¶§§§§§§¶¶
# ________¶¶¶§ƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒ§§§§§§¶¶_______¶¶§§§§§§¶¶
# _________¶¶ƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒ§§§§¶¶¶¶____¶¶¶¶§§§§§§§§§§¶¶
# _________¶¶ƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒ§§¶¶§§¶¶¶¶¶¶ƒƒ§§§§§§§§¶¶¶¶
# ________¶¶ƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒ§§§§§§§¶¶ƒƒƒƒ§§§§§§¶¶¶¶
# ________¶¶ƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒ§§§§§§§§¶¶§§§§§§§¶¶¶¶
# __¶¶¶¶¶¶¶¶¶ƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒ§§§§§§§§§¶¶§§§§§§¶¶
# _¶¶ƒƒ¶¶ƒƒƒ¶¶ƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒ§§§§§§§§§¶¶¶¶§§§§§§¶¶
# _¶¶ƒƒƒ¶¶ƒƒƒ¶¶ƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒ§§§§§§§§§§¶¶__¶¶¶###§§§¶¶
# __¶¶§§§§§§§§¶¶ƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒ§§§§§§§§§§§§§¶¶¶¶¶#######§§§¶¶
# ___¶¶§§§§§§§§¶¶ƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒƒ§§§§§§§§§§§§§§§§§########¶¶¶¶¶¶
# ____¶¶§§§§§§§§¶¶§§§§ƒƒƒƒƒƒƒ§§§§§§§§§§§§§§§§§§§####¶¶¶¶¶¶
# _____¶¶§§§§§§§¶¶§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§¶¶¶¶
# _______¶¶¶¶¶¶¶§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§¶¶
# ______________¶¶¶¶¶¶¶¶¶¶§§§§§§§§§§§§§§§§§§§§¶¶
# ________________________¶¶¶¶¶¶§§§§§§§§§§¶¶¶¶
# ____________________________¶¶¶¶§§§§¶¶¶¶¶
# ____________________________¶¶§§§§§§§§¶¶
# ____________________________¶¶§§¶¶§§§¶¶
# _____________________________¶¶§¶¶§§¶¶
# ______________________________¶¶¶¶¶¶
# ---


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

        vpc_environment = environments.get("webserver_vpc")
        vpc_name = vpc_environment.get("name")
        max_azs = vpc_environment.get("max_az")
        cidr = vpc_environment.get("cidr")
        subnet_name = vpc_environment.get("subnet_name")
        cidr_mask = vpc_environment.get("cidr_mask")

        second_vpc_environment = environments.get("managementserver_vpc")
        second_vpc_name = second_vpc_environment.get("name")
        second_max_azs = second_vpc_environment.get("max_az")
        second_cidr = second_vpc_environment.get("cidr")
        second_subnet_name = second_vpc_environment.get("subnet_name")
        second_cidr_mask = second_vpc_environment.get("cidr_mask")

        peering_environment = environments.get("peering")
        peering_name = peering_environment.get("name")
        peer_region = peering_environment.get("peer_region")

        route_environment = environments.get("route")
        route_name = route_environment.get("name")

        second_route_environment = environments.get("second_route")
        second_route_name = second_route_environment.get("name")

        role_environment = environments.get("role")
        role_name = role_environment.get("name")
        role_service_principal = role_environment.get("role_service_principal")
        role_managed_policy_name = role_environment.get("role_managed_policy_name")

        mm_sg_environment = environments.get("management_security_group")
        mm_sg_name = mm_sg_environment.get("name")
        mm_sg_description = mm_sg_environment.get("description")
        mm_sg_ob = mm_sg_environment.get("allow_all_outbound")

        mm_sg_ssh_ipv4 = mm_sg_environment.get("ssh_allowed_ipv4")
        mm_sg_ssh_port = mm_sg_environment.get("ssh_allowed_port")
        mm_sg_ing_ssh_desc = mm_sg_environment.get("ssh_port_description")

        mm_sg_rdp_ipv4 = mm_sg_environment.get("rdp_allowed_ipv4")
        mm_sg_rdp_port = mm_sg_environment.get("rdp_allowed_port")
        mm_sg_rdp_ssh_desc = mm_sg_environment.get("rdp_port_description")

        wb_sg_environment = environments.get("webserver_security_group")
        wb_sg_name = wb_sg_environment.get("name")
        wb_sg_description = wb_sg_environment.get("description")
        wb_sg_ob = wb_sg_environment.get("allow_all_outbound")

        wb_sg_http_port = wb_sg_environment.get("http_allowed_port")
        wb_sg_http_desc = wb_sg_environment.get("http_port_description")

        wb_sg_https_port = wb_sg_environment.get("https_allowed_port")
        wb_sg_https_desc = wb_sg_environment.get("https_port_description")

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

        webinstance_enviroment = environments.get("webserver_instance")
        webinstance_name = webinstance_enviroment.get("name")
        webinstance_type = webinstance_enviroment.get("instance_type")
        webinstance_avz = webinstance_enviroment.get("availability_zone")
        webinstance_root = webinstance_enviroment.get("root_device_directory")
        webinstance_size = webinstance_enviroment.get("volume_size")
        webinstance_encrypt = webinstance_enviroment.get("encrypted_volume")
        webinstance_asset = webinstance_enviroment.get("asset_bucket")
        webinstance_path = webinstance_enviroment.get("asset_path")
        webinstance_region = webinstance_enviroment.get("asset_region")

        # mminstance_enviroment = environments.get("managementserver_instance")
        # mminstance_name = mminstance_enviroment.get("name")
        # mminstance_type = mminstance_enviroment.get("instance_type")
        # mminstance_avz = mminstance_enviroment.get("availability_zone")
        # mminstance_root = mminstance_enviroment.get("root_device_directory")
        # mminstance_size = mminstance_enviroment.get("volume_size")
        # mminstance_encrypt = mminstance_enviroment.get("encrypted_volume")
        #
        # web_bk_environment = environments.get("webserver_backup")
        # web_bk_backup = web_bk_environment.get("name")
        # web_bk_name = web_bk_environment.get("backup_plan_name")
        # web_bk_vault = web_bk_environment.get("backup_vault_name")
        # web_bk_rule = web_bk_environment.get("backup_rule_name")
        # web_bk_del = web_bk_environment.get("delete_backup_after_days")
        # web_bk_min = web_bk_environment.get("cron_minute")
        # web_bk_hour = web_bk_environment.get("cron_hour")
        # web_bk_month = web_bk_environment.get("cron_month")
        # web_bk_week = web_bk_environment.get("cron_week_day")
        # web_bk_year = web_bk_environment.get("cron_year")
        # web_bk_select = web_bk_environment.get("backup_selection_name")
        #
        # man_bk_environment = environments.get("managementserver_backup")
        # man_bk_backup = man_bk_environment.get("name")
        # man_bk_name = man_bk_environment.get("backup_plan_name")
        # man_bk_vault = man_bk_environment.get("backup_vault_name")
        # man_bk_rule = man_bk_environment.get("backup_rule_name")
        # man_bk_del = man_bk_environment.get("delete_backup_after_days")
        # man_bk_min = man_bk_environment.get("cron_minute")
        # man_bk_hour = man_bk_environment.get("cron_hour")
        # man_bk_month = man_bk_environment.get("cron_month")
        # man_bk_week = man_bk_environment.get("cron_week_day")
        # man_bk_year = man_bk_environment.get("cron_year")
        # man_bk_select = man_bk_environment.get("backup_selection_name")

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
            )
            ]
        )

        # vpc creation for management server, includes 2 public subnets and 2 az.

        # vpc2 = ec2.Vpc(
        #     self, vpc_name,
        #     max_azs=max_azs,
        #     cidr=cidr,
        #     # configuration will create 2 groups in 2 AZs = 4 subnets.
        #     subnet_configuration=[ec2.SubnetConfiguration(
        #         subnet_type=ec2.SubnetType.PUBLIC,
        #         name=subnet_name,
        #         cidr_mask=cidr_mask
        #     )
        #     ]
        # )
        #
        # # Deployment of vpc-peering.
        #
        # Peering_connection = ec2.CfnVPCPeeringConnection(
        #     self, peering_name,
        #     peer_vpc_id=vpc1.vpc_id,
        #     vpc_id=vpc2.vpc_id,
        #
        #     # the properties below are optional
        #     peer_region=peer_region,
        # )
        #
        # ec2.CfnRoute(
        #     self, route_name,
        #     route_table_id=vpc1.public_subnets[0].route_table.route_table_id,
        #     destination_cidr_block=vpc2.vpc_cidr_block,
        #     vpc_peering_connection_id=Peering_connection.ref
        # )
        #
        # ec2.CfnRoute(
        #     self, second_route_name,
        #     route_table_id=vpc2.public_subnets[1].route_table.route_table_id,
        #     destination_cidr_block=vpc1.vpc_cidr_block,
        #     vpc_peering_connection_id=Peering_connection.ref
        # )

        # Linux AMI creation.

        amzn_linux = ec2.MachineImage.latest_amazon_linux(
            generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2,
            edition=ec2.AmazonLinuxEdition.STANDARD,
            virtualization=ec2.AmazonLinuxVirt.HVM,
            storage=ec2.AmazonLinuxStorage.GENERAL_PURPOSE,
        )

        # Windows AMI creation.

        # windows = ec2.MachineImage.latest_windows(ec2.WindowsVersion.WINDOWS_SERVER_2019_ENGLISH_FULL_BASE)

        # Role creation.

        role = iam.Role(self, role_name, assumed_by=iam.ServicePrincipal(role_service_principal))

        role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name(role_managed_policy_name))

        # Security group creation for management server.

        # Management_sg = ec2.SecurityGroup(
        #     self, mm_sg_name,
        #     vpc=vpc2,
        #     description=mm_sg_description,
        #     allow_all_outbound=mm_sg_ob
        # )
        #
        # Management_sg.add_ingress_rule(ec2.Peer.ipv4(mm_sg_ssh_ipv4), ec2.Port.tcp(mm_sg_ssh_port), mm_sg_ing_ssh_desc)
        # Management_sg.add_ingress_rule(ec2.Peer.ipv4(mm_sg_rdp_ipv4), ec2.Port.tcp(mm_sg_rdp_port), mm_sg_rdp_ssh_desc)

        # Security group creation for webserver.

        Webserver_sg = ec2.SecurityGroup(
            self, wb_sg_name,
            vpc=vpc1,
            description=wb_sg_description,
            allow_all_outbound=wb_sg_ob
        )

        Webserver_sg.add_ingress_rule(ec2.Peer.any_ipv4(), ec2.Port.tcp(80),
                                      "Allow HTTP traffic to ELB")
        #
        Webserver_sg.add_ingress_rule(ec2.Peer.any_ipv4(), ec2.Port.tcp(443),
                                      "Allow HTTPS traffic to ELB")

        # Webserver_sg.add_egress_rule(ec2.Peer.security_group_id(elb_sg.security_group_id), ec2.Port.tcp(80), "Allow  HTTP outbound traffic to ELB")
        #
        # Webserver_sg.add_egress_rule(ec2.Peer.security_group_id(elb_sg.security_group_id), ec2.Port.tcp(443),"Allow HTTPS outbound traffic to ELB")

        # Webserver_sg.add_ingress_rule(ec2.Peer.security_group_id(Management_sg.security_group_id),
        #                               ec2.Port.tcp(wb_sg_ssh_port), wb_sg_ssh_desc)

        # Create a key pair with lambda function that will store the public and private key in secrets manager

        # Create a key pair for the management server.

        # mmkey = KeyPair(
        #     self, mm_key_name,
        #     name=mm_key_name,
        #     description=mm_key_desc,
        #     store_public_key=mm_key_store)
        #
        # mmkey.grant_read_on_private_key(role)
        # mmkey.grant_read_on_public_key(role)

        # Create a key pair for the webserver.

        webkey = KeyPair(
            self, web_key_name,
            name=web_key_name,
            description=web_key_desc,
            store_public_key=web_key_store)

        webkey.grant_read_on_private_key(role)
        webkey.grant_read_on_public_key(role)

        # ec2 instance creation for the webserver.

        # Webserver = ec2.Instance(
        #     self, webinstance_name,
        #     instance_type=ec2.InstanceType(webinstance_type),
        #     machine_image=amzn_linux,
        #     security_group=Webserver_sg,
        #     vpc=vpc1,
        #     # user_data=ec2.UserData.custom(user_data),
        #     availability_zone=webinstance_avz,
        #     # key_name=webkey.key_pair_name,
        #     block_devices=[ec2.BlockDevice(
        #         device_name=webinstance_root,
        #         volume=ec2.BlockDeviceVolume.ebs(webinstance_size,
        #                                          encrypted=webinstance_encrypt
        #                                          )
        #     )
        #     ]
        # )

        self.asg = autoscaling.AutoScalingGroup(
            self, "WebServer",
            instance_type=ec2.InstanceType(webinstance_type),
            associate_public_ip_address=False,
            machine_image=amzn_linux,
            security_group=Webserver_sg,
            vpc=vpc1,
            key_name=webkey.key_pair_name,
            block_devices=[autoscaling.BlockDevice(
                device_name=webinstance_root,
                volume=autoscaling.BlockDeviceVolume.ebs(webinstance_size,
                                                         encrypted=webinstance_encrypt
                                                         )
            )
            ],
            # health_check=autoscaling.HealthCheck.ec2(
            #     grace=cdk.Duration.minutes(2),
            # ),
            desired_capacity=1,
            min_capacity=1,
            max_capacity=3,
        )

        self.asg.scale_on_cpu_utilization(
            "scale_on_cpu",
            target_utilization_percent=50
        )

        lb = elbv2.ApplicationLoadBalancer(
            self, "lb_name",
            vpc=vpc1,
            internet_facing=True,
            load_balancer_name="MyALB"
        )


        listener_certificate = elbv2.ListenerCertificate.from_arn(
            "arn:aws:acm:eu-central-1:600563666729:certificate/a0f96b13-cd78-4305-a3df-f28430dac0a9")

        tg = elbv2.ApplicationTargetGroup(
            self, "tg_name",
            vpc=vpc1,
            port=80,
            protocol=elbv2.ApplicationProtocol.HTTP,
            target_type=elbv2.TargetType.INSTANCE,
            targets=[self.asg],
            health_check=elbv2.HealthCheck(
                path="/index.html",
                port="80",
                protocol=elbv2.Protocol.HTTP
            )
        )

        listener = lb.add_listener(
            "listener_name",
            certificates=[listener_certificate],
            port=443,
            default_target_groups=[tg],
            protocol=elbv2.ApplicationProtocol.HTTPS,
            open=True,
            ssl_policy=SslPolicy.RECOMMENDED
        )

        Webserver_sg.connections.allow_from(listener, ec2.Port.tcp(wb_sg_http_port),
                                            "Allow HTTP inbound traffic from ELB")
        Webserver_sg.connections.allow_from(listener, ec2.Port.tcp(wb_sg_https_port),
                                            "Allow HTTPS inbound traffic from ELB")

        lb.add_redirect(
            source_port=80,
            target_port=443
        )

        # listener.add_targets(
        #     "target_name",
        #     port=80,
        #     targets=[asg]
        # protocol=elbv2.ApplicationProtocol.HTTP,
        # targetType=elbv2.TargetType.INSTANCE,
        # health_check=elbv2.HealthCheck(
        #     path="/index.html",
        #     port="80",
        #     protocol=elbv2.Protocol.HTTP,
        # )
        # )

        elb_sg = ec2.SecurityGroup(
            self, "elb_sg",
            vpc=vpc1,
            description=wb_sg_description,
            allow_all_outbound=wb_sg_ob
        )

        # listener.connections.allow_default_port_from_any_ipv4("AllowAll")

        # Add userdata to the webserver.

        assets = Asset(self, webinstance_asset,
                       path=webinstance_path
                       )

        Local_path = self.asg.user_data.add_s3_download_command(
            bucket=assets.bucket,
            bucket_key=assets.s3_object_key,
            region=webinstance_region,
        )

        self.asg.user_data.add_execute_file_command(
            file_path=Local_path
        )

        assets.grant_read(self.asg.role)

        # elb_sg.add_ingress_rule(ec2.Peer.any_ipv4(), ec2.Port.tcp(wb_sg_http_port), wb_sg_http_desc)

        elb_sg.add_ingress_rule(ec2.Peer.any_ipv4(), ec2.Port.all_traffic(), "Allow all traffic")

        listener.connections.add_security_group(elb_sg)
        listener.connections.allow_from_any_ipv4(ec2.Port.tcp(80), "Allow HTTP inbound traffic from ELB")


'''
        # ec2 instance creation for the management server.

        ManagementServer = ec2.Instance(
            self, mminstance_name,
            instance_type=ec2.InstanceType(mminstance_type),
            machine_image=windows,
            vpc=vpc2,
            security_group=Management_sg,
            availability_zone=mminstance_avz,
            key_name=mmkey.key_pair_name,
            block_devices=[ec2.BlockDevice(
                device_name=mminstance_root,
                volume=ec2.BlockDeviceVolume.ebs(mminstance_size,
                                                 encrypted=mminstance_encrypt
                                                 )
            )
            ]
        )

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
                bk.BackupResource.from_ec2_instance(Webserver)
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
'''
