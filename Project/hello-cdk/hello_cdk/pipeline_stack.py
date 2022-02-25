from constructs import Construct
from aws_cdk import (
    Stack,
    aws_codecommit as codecommit,
    pipelines as pipelines
)

from .pipeline_stage import WorkshopPipelineStage


class WorkshopPipelineStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        repo = codecommit.Repository(
            self, "WorkshopRepo",
            repository_name="workshop-repo")

        # Pipeline code will go here

        pipeline = pipelines.CodePipeline(
            self, "WorkshopPipeline",
            synth=pipelines.ShellStep(
                "Synth",
                input=pipelines.CodePipelineSource.code_commit(repo, "master"),
                commands=[
                    "npm install -g aws-cdk",  # Install CDK
                    "pip install -r requirements.txt",  # Install Python dependencies
                    "npx cdk synth"  # Run CDK synth
                ]
            ),
        )

        deploy = WorkshopPipelineStage(self, "Deploy", )
        deploy_stage = pipeline.add_stage(deploy)