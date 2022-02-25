from constructs import Construct
from aws_cdk import (
    Stage
)
from .pipeline_stack import WorkshopPipelineStack


class WorkshopPipelineStage(Stage):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        service = WorkshopPipelineStack(self, "WebService")
