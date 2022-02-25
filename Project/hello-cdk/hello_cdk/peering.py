import aws_cdk as cdk
from aws_cdk import (
    Stack,
    aws_s3 as s3,
    aws_iam as iam,
    aws_s3_deployment as s3deploy
)
from constructs import Construct


class PeeringStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        bucket = s3.Bucket(
            self, "Bucket",
            versioned=True,
            removal_policy=cdk.RemovalPolicy.DESTROY,
            encryption=s3.BucketEncryption.KMS_MANAGED,
            auto_delete_objects=True
        )

        s3deploy.BucketDeployment(
            self, "S3Deployment",
            sources=[s3deploy.Source.asset("./hello_cdk/user_data")],
            destination_bucket=bucket,
        )


