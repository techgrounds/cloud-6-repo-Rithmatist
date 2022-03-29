import aws_cdk as cdk
from constructs import Construct
from cdk_ec2_key_pair import KeyPair
from aws_cdk import (
    aws_ec2 as ec2,
)


class ManagementServer(cdk.NestedStack):
    def __init__(self, scope: Construct, id: str,
                 vpc: ec2.Vpc,
                 Management_sg: ec2.SecurityGroup,
                 **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        environments = self.node.try_get_context("ENVIRONMENTS")
        mm_key_env = environments.get('management_key_pair')
        mm_key_name = mm_key_env.get('name')
        mm_key_desc = mm_key_env.get('description')
        mm_key_store = mm_key_env.get('store_public_key')

        mm_instance_environment = environments.get("managementserver_instance")
        mm_instance_name = mm_instance_environment.get("name")
        mm_instance_type = mm_instance_environment.get("instance_type")
        mm_instance_avz = mm_instance_environment.get("availability_zone")
        mm_instance_root = mm_instance_environment.get("root_device_directory")
        mm_instance_size = mm_instance_environment.get("volume_size")
        mm_instance_encrypt = mm_instance_environment.get("encrypted_volume")

        # Create a key pair with lambda function that will store the public and private key in secrets manager

        # Create a key pair for the management server.

        mm_key = KeyPair(
            scope=scope,
            id=mm_key_name,
            name=mm_key_name,
            description=mm_key_desc,
            store_public_key=mm_key_store)

        windows = ec2.MachineImage.latest_windows(ec2.WindowsVersion.WINDOWS_SERVER_2019_ENGLISH_FULL_BASE)

        self.ManagementServer = ec2.Instance(
            self, mm_instance_name,
            instance_type=ec2.InstanceType(mm_instance_type),
            machine_image=windows,
            vpc=vpc,
            security_group=Management_sg,
            availability_zone=mm_instance_avz,
            key_name=mm_key.key_pair_name,
            block_devices=[ec2.BlockDevice(
                device_name=mm_instance_root,
                volume=ec2.BlockDeviceVolume.ebs(mm_instance_size,
                                                 encrypted=mm_instance_encrypt
                                                 )
            )
            ]
        )

