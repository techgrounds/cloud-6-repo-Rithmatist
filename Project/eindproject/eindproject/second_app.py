from aws_cdk.aws_s3_assets import Asset
from cdk_ec2_key_pair import KeyPair
import aws_cdk as cdk
from constructs import Construct
from aws_cdk import (
    aws_autoscaling as autoscaling,
    aws_ec2 as ec2
)


class WebServer(cdk.NestedStack):
    def __init__(self, scope: Construct, id: str,
                 Webserver_sg: ec2.SecurityGroup,
                 vpc: ec2.Vpc,
                 **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        environments = self.node.try_get_context("ENVIRONMENTS")
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

        # Create a key pair for the webserver.

        web_key = KeyPair(
            self,
            web_key_name,
            name=web_key_name,
            description=web_key_desc,
            resource_prefix="web_key",
            store_public_key=web_key_store)

        aws_linux = ec2.MachineImage.latest_amazon_linux(
            generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2,
            edition=ec2.AmazonLinuxEdition.STANDARD,
            virtualization=ec2.AmazonLinuxVirt.HVM,
            storage=ec2.AmazonLinuxStorage.GENERAL_PURPOSE,
        )

        self.asg = autoscaling.AutoScalingGroup(
            self,
            web_instance_name,
            instance_type=ec2.InstanceType(web_instance_type),
            machine_image=aws_linux,
            security_group=Webserver_sg,
            vpc=vpc,
            key_name=web_key.key_pair_name,
            block_devices=[autoscaling.BlockDevice(
                device_name=web_instance_root,
                volume=autoscaling.BlockDeviceVolume.ebs(web_instance_size,
                                                         encrypted=web_instance_encrypt
                                                         )
            )
            ],
            desired_capacity=1,
            min_capacity=1,
            max_capacity=3,
        )

        web_key.grant_read_on_private_key(self.asg.role)
        web_key.grant_read_on_public_key(self.asg.role)

        assets = Asset(self, web_instance_asset,
                       path=web_instance_path
                       )

        Local_path = self.asg.user_data.add_s3_download_command(
            bucket=assets.bucket,
            bucket_key=assets.s3_object_key,
            region=web_instance_region,
        )

        self.asg.user_data.add_execute_file_command(
            file_path=Local_path
        )

        assets.grant_read(self.asg.role)
