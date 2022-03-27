#!/usr/bin/env python3

import aws_cdk as cdk
from hello_cdk.vpc_stack import VpcStack
from hello_cdk.ec2_stack import Ec2Stack
from hello_cdk.Backups_stack import BackupStack
from hello_cdk.S3Bucket_stack import S3BucketStack
from hello_cdk.peering_stack import VpcPeeringStack
from hello_cdk.autoscaling_elb_stack import AutoScalingElbStack

app = cdk.App()
main_stack = cdk.Stack(app, "MainStack", env=cdk.Environment(account='600563666729', region='eu-central-1'))
bucket_stack = S3BucketStack(main_stack, "S3 Bucket App")
skeleton = VpcStack(main_stack, "vpc app")
ec2_app = Ec2Stack(
    main_stack,
    "Instance app",
    vpc=skeleton.vpc2
)
LoadBalancer_app = AutoScalingElbStack(
    main_stack,
    "LoadBalancer App",
    vpc=skeleton.vpc1
)
peering_app = VpcPeeringStack(
    main_stack,
    "Vpc Peering App",
    vpc1=skeleton.vpc1,
    vpc2=skeleton.vpc2,
    Webserver_sg=LoadBalancer_app.Webserver_sg,
    Management_sg=ec2_app.Management_sg,
)
Backup_app = BackupStack(
    main_stack,
    "Backup App",
    ManagementServer=ec2_app.ManagementServer,
    asg=LoadBalancer_app.asg
)


app.synth()
