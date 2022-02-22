import aws_cdk as cdk
from aws_cdk import aws_secretsmanager as secretsmanager
from aws_cdk import (
    Stack,
    aws_iam as iam
)
from constructs import Construct


class iamusers(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create a new secret
        secret = secretsmanager.Secret(
            self, "Secret",
            description="My secret",
            secret_name="mysecret"
        )

        # Create a new user

        admin = iam.User(
            self, "Admin",
            user_name="admin",
            password=secret.secret_value
        )

        # Add a managed policy to the user
        admin.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name(
                "AdministratorAccess"
            )
        )

        admin_group = iam.Group(
            self, "AdminGroup",
            group_name="admin-group"
        )

        output_1 = cdk.CfnOutput(
            self, "user2LoginUrl",
            description="LoginUrl for User2",
            value=f"https://{cdk.Aws.ACCOUNT_ID}.signin.aws.amazon.com/console"
        )
