import aws_cdk as cdk
from constructs import Construct
from aws_cdk import (
    aws_ec2 as ec2,
)


class VpcPeeringStack(cdk.NestedStack):
    def __init__(self, scope: Construct, id: str, vpc1: ec2.Vpc, vpc2: ec2.Vpc, Webserver_sg: ec2.SecurityGroup,
                 Management_sg: ec2.SecurityGroup, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        environments = self.node.try_get_context("ENVIRONMENTS")
        peering_environment = environments.get("peering")
        peering_name = peering_environment.get("name")
        peer_region = peering_environment.get("peer_region")

        route_environment = environments.get("route")
        route_name = route_environment.get("name")

        second_route_environment = environments.get("second_route")
        second_route_name = second_route_environment.get("name")

        third_route_environment = environments.get("third_route")
        third_route_name = third_route_environment.get("name")

        wb_sg_environment = environments.get("webserver_security_group")
        wb_sg_ssh_port = wb_sg_environment.get("ssh_allowed_port")
        wb_sg_ssh_desc = wb_sg_environment.get("ssh_port_description")

        Peering_connection = ec2.CfnVPCPeeringConnection(
            self, peering_name,
            peer_vpc_id=vpc1.vpc_id,
            vpc_id=vpc2.vpc_id,

            # the properties below are optional
            peer_region=peer_region,
        )
        #

        for i in range(0, 2):
            ec2.CfnRoute(self, route_name + str(i),
                         route_table_id=vpc1.public_subnets[i].route_table.route_table_id,
                         destination_cidr_block=vpc2.vpc_cidr_block,
                         vpc_peering_connection_id=Peering_connection.ref
                         )

        for i in range(0, 2):
            ec2.CfnRoute(self, second_route_name + str(i),
                         route_table_id=vpc1.private_subnets[i].route_table.route_table_id,
                         destination_cidr_block=vpc2.vpc_cidr_block,
                         vpc_peering_connection_id=Peering_connection.ref
                         )

        for i in range(0, 2):
            ec2.CfnRoute(self, third_route_name + str(i),
                         route_table_id=vpc2.public_subnets[i].route_table.route_table_id,
                         destination_cidr_block=vpc1.vpc_cidr_block,
                         vpc_peering_connection_id=Peering_connection.ref
                         )

        Webserver_sg.add_ingress_rule(ec2.Peer.security_group_id(Management_sg.security_group_id),
                                      ec2.Port.tcp(wb_sg_ssh_port), wb_sg_ssh_desc)
