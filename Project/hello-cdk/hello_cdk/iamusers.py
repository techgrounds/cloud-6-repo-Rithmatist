import aws_cdk as cdk
import os.path
from cdk_ec2_key_pair import KeyPair
from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_iam as iam,
    aws_s3 as s3,
    aws_backup as bk,
    aws_events as event,
    aws_s3_deployment as s3deploy,
    custom_resources as cr,
)
from constructs import Construct


class iamusers(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)