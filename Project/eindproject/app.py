#!/usr/bin/env python3
from eindproject.security_groups import SecurityGroups
from eindproject.vpc_peering import VpcPeeringStack
from eindproject.load_balancer import LoadBalancer
from eindproject.first_app import ManagementServer
from eindproject.s3bucket import S3BucketStack
from eindproject.second_app import WebServer
from eindproject.backups import BackupStack
from eindproject.vpcs import VpcStack
import aws_cdk as cdk

app = cdk.App()
main = cdk.Stack(app, "main", env=cdk.Environment(account='600563666729', region='eu-central-1'))
s3bucket = S3BucketStack(main, "S3 Bucket App")
skeleton = VpcStack(main, "vpc app")
sg_app = SecurityGroups(
    main,
    "Security Groups",
    vpc1=skeleton.vpc1,
    vpc2=skeleton.vpc2
)
first_app = ManagementServer(
    main,
    "Management Server",
    Management_sg=sg_app.Management_sg,
    vpc=skeleton.vpc2
)
second_app = WebServer(
    main,
    "Web Server",
    Webserver_sg=sg_app.Webserver_sg,
    vpc=skeleton.vpc1
)
vpc_peering = VpcPeeringStack(
    main,
    "Vpc Peering App",
    vpc1=skeleton.vpc1,
    vpc2=skeleton.vpc2,
    Webserver_sg=sg_app.Webserver_sg,
    Management_sg=sg_app.Management_sg,
)
elb_app = LoadBalancer(
    main,
    "Load Balancer",
    vpc=skeleton.vpc1,
    asg=second_app.asg
)
Backup_app = BackupStack(
    main,
    "Backup App",
    ManagementServer=first_app.ManagementServer,
    asg=second_app.asg
)

app.synth()
