import aws_cdk as cdk
from constructs import Construct
from aws_cdk import (
    aws_ec2 as ec2,
)


class VpcStack(cdk.NestedStack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        environments = self.node.try_get_context("ENVIRONMENTS")
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

        self.vpc1 = ec2.Vpc(
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

        self.vpc2 = ec2.Vpc(
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