from constructs import Construct
from aws_cdk import (
    Stack,
    aws_codecommit as codecommit
)
from aws_cdk.aws_codepipeline import (
    Artifact,
    Pipeline
)


class WorkshopPipelineStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        repo = codecommit.Repository(self, "WorkshopRepo",
                                     repository_name="workshop-repo")


        # Pipeline code will go here
