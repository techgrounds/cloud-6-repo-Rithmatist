#!/usr/bin/env python3

from eindproject.vpc_peering import VpcPeeringStack
from eindproject.first_app import ManagementServer
from eindproject.s3bucket import S3BucketStack
from eindproject.second_app import WebServer
from eindproject.backups import BackupStack
from eindproject.vpcs import VpcStack
import aws_cdk as cdk

app = cdk.App()
main_stack = cdk.Stack(app, "MainStack", env=cdk.Environment(account='600563666729', region='eu-central-1'))
s3bucket = S3BucketStack(main_stack, "S3 Bucket App")
skeleton = VpcStack(main_stack, "vpc app")
first_app = ManagementServer(
    main_stack,
    "Management Server",
    vpc=skeleton.vpc2
)
second_app = WebServer(
    main_stack,
    "Web Server",
    vpc=skeleton.vpc1
)
vpc_peering = VpcPeeringStack(
    main_stack,
    "Vpc Peering App",
    vpc1=skeleton.vpc1,
    vpc2=skeleton.vpc2,
    Webserver_sg=second_app.Webserver_sg,
    Management_sg=first_app.Management_sg,
)
Backup_app = BackupStack(
    main_stack,
    "Backup App",
    ManagementServer=first_app.ManagementServer,
    asg=second_app.asg
)


app.synth()
