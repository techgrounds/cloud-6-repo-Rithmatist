import aws_cdk as cdk
from constructs import Construct
from aws_cdk import (
    aws_s3_deployment as s3deploy,
    aws_s3 as s3,
)


class S3BucketStack(cdk.NestedStack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        environments = self.node.try_get_context("ENVIRONMENTS")
        Bucket_environment = environments.get("bucket")
        bucket_name = Bucket_environment.get("bucket_name")
        versioned = Bucket_environment.get("versioned")
        auto_delete_objects = Bucket_environment.get("auto_delete_objects")

        s3deploy_environment = environments.get("s3deploy")
        s3Deployment_name = s3deploy_environment.get("name")
        sources = s3deploy_environment.get("sources")

        bucket = s3.Bucket(
            self,
            bucket_name,
            versioned=versioned,
            removal_policy=cdk.RemovalPolicy.DESTROY,
            encryption=s3.BucketEncryption.KMS_MANAGED,
            auto_delete_objects=auto_delete_objects
        )

        # S3 Bucket file deployment.

        s3deploy.BucketDeployment(
            self, s3Deployment_name,
            sources=[s3deploy.Source.asset(sources)],
            destination_bucket=bucket
        )