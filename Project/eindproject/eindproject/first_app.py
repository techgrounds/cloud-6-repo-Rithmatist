import aws_cdk as cdk
from constructs import Construct
from aws_cdk import (
    aws_ec2 as ec2,
)


class ManagementServer(cdk.NestedStack):
    def __init__(self, scope: Construct, id: str,
                 vpc: ec2.Vpc,
                 **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        environments = self.node.try_get_context("ENVIRONMENTS")
        mm_sg_environment = environments.get("management_security_group")
        mm_sg_name = mm_sg_environment.get("name")
        mm_sg_description = mm_sg_environment.get("description")
        mm_sg_ob = mm_sg_environment.get("allow_all_outbound")

        allowed_ipv4 = mm_sg_environment.get("allowed_ipv4")
        mm_sg_ssh_port = mm_sg_environment.get("ssh_allowed_port")
        mm_sg_ing_ssh_desc = mm_sg_environment.get("ssh_port_description")
        mm_sg_rdp_port = mm_sg_environment.get("rdp_allowed_port")
        mm_sg_rdp_ssh_desc = mm_sg_environment.get("rdp_port_description")

        mm_instance_environment = environments.get("managementserver_instance")
        mm_instance_name = mm_instance_environment.get("name")
        mm_instance_type = mm_instance_environment.get("instance_type")
        mm_instance_avz = mm_instance_environment.get("availability_zone")
        mm_instance_root = mm_instance_environment.get("root_device_directory")
        mm_instance_size = mm_instance_environment.get("volume_size")
        mm_instance_encrypt = mm_instance_environment.get("encrypted_volume")

        self.Management_sg = ec2.SecurityGroup(
            self, mm_sg_name,
            vpc=vpc,
            description=mm_sg_description,
            allow_all_outbound=mm_sg_ob
        )

        allowed_ips = allowed_ipv4
        for i in range(len(allowed_ips)):
            self.Management_sg.add_ingress_rule(ec2.Peer.ipv4(allowed_ips[i] + "/32"), ec2.Port.tcp(mm_sg_ssh_port),
                                           mm_sg_ing_ssh_desc)

        for i in range(len(allowed_ips)):
            self.Management_sg.add_ingress_rule(ec2.Peer.ipv4(allowed_ips[i] + "/32"), ec2.Port.tcp(mm_sg_rdp_port),
                                           mm_sg_rdp_ssh_desc)

        windows = ec2.MachineImage.latest_windows(ec2.WindowsVersion.WINDOWS_SERVER_2019_ENGLISH_FULL_BASE)

        self.ManagementServer = ec2.Instance(
            self, mm_instance_name,
            instance_type=ec2.InstanceType(mm_instance_type),
            machine_image=windows,
            vpc=vpc,
            security_group=self.Management_sg,
            availability_zone=mm_instance_avz,
            # key_name="mm_key",
            block_devices=[ec2.BlockDevice(
                device_name=mm_instance_root,
                volume=ec2.BlockDeviceVolume.ebs(mm_instance_size,
                                                 encrypted=mm_instance_encrypt
                                                 )
            )
            ]
        )

