import aws_cdk as cdk
from constructs import Construct
from aws_cdk import (
    aws_ec2 as ec2,
)


class SecurityGroups(cdk.NestedStack):
    def __init__(self, scope: Construct, id: str,
                 vpc1: ec2.Vpc,
                 vpc2: ec2.Vpc,
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

        wb_sg_environment = environments.get("webserver_security_group")
        wb_sg_name = wb_sg_environment.get("name")
        wb_sg_description = wb_sg_environment.get("description")
        wb_sg_ob = wb_sg_environment.get("allow_all_outbound")

        self.Management_sg = ec2.SecurityGroup(
            self,
            mm_sg_name,
            vpc=vpc2,
            description=mm_sg_description,
            security_group_name=mm_sg_name,
            allow_all_outbound=mm_sg_ob
        )

        allowed_ips = allowed_ipv4
        for i in range(len(allowed_ips)):
            self.Management_sg.add_ingress_rule(ec2.Peer.ipv4(allowed_ips[i] + "/32"), ec2.Port.tcp(mm_sg_ssh_port),
                                                mm_sg_ing_ssh_desc)

        for i in range(len(allowed_ips)):
            self.Management_sg.add_ingress_rule(ec2.Peer.ipv4(allowed_ips[i] + "/32"), ec2.Port.tcp(mm_sg_rdp_port),
                                                mm_sg_rdp_ssh_desc)

        self.Webserver_sg = ec2.SecurityGroup(
            self,
            wb_sg_name,
            vpc=vpc1,
            security_group_name=wb_sg_name,
            description=wb_sg_description,
            allow_all_outbound=wb_sg_ob
        )

        self.Webserver_sg.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.tcp(80),
            description="Allow HTTP traffic from the world"
        )
