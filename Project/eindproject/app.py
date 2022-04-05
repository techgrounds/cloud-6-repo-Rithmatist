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
StackName = "main"
account = "600563666729"
region = "eu-central-1"
ManagementServerStackName = "Management Server App"
SecurityGroupStackName = "Security Group App"
LoadBalancerStackName = "Load Balancer App"
VpcPeeringStackName = "VPC Peering App"
WebServerStackName = "Web Server App"
S3BucketStackName = "S3 Bucket App"
BackupStackName = "Backup App"
VpcStackName = "VPC App"

main = cdk.Stack(app, StackName, env=cdk.Environment(account=account, region=region))
s3bucket = S3BucketStack(main, S3BucketStackName)
skeleton = VpcStack(main, VpcStackName)
sg_app = SecurityGroups(
    main,
    SecurityGroupStackName,
    vpc1=skeleton.vpc1,
    vpc2=skeleton.vpc2
)
first_app = ManagementServer(
    main,
    ManagementServerStackName,
    Management_sg=sg_app.Management_sg,
    vpc=skeleton.vpc2
)
second_app = WebServer(
    main,
    WebServerStackName,
    Webserver_sg=sg_app.Webserver_sg,
    vpc=skeleton.vpc1
)
vpc_peering = VpcPeeringStack(
    main,
    VpcPeeringStackName,
    vpc1=skeleton.vpc1,
    vpc2=skeleton.vpc2,
    Webserver_sg=sg_app.Webserver_sg,
    Management_sg=sg_app.Management_sg,
)
elb_app = LoadBalancer(
    main,
    LoadBalancerStackName,
    vpc=skeleton.vpc1,
    asg=second_app.asg
)
Backup_app = BackupStack(
    main,
    BackupStackName,
    ManagementServer=first_app.ManagementServer,
    asg=second_app.asg
)

app.synth()
