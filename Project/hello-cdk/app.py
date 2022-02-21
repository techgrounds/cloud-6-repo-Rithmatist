#!/usr/bin/env python3
import os

import aws_cdk as cdk

from hello_cdk.hello_cdk_stack import CdkVpcStack
from hello_cdk.Peering import PeeringStack
from hello_cdk.iamusers import iamusers

app = cdk.App()
CdkVpcStack(app, "HelloCdkStack", env=cdk.Environment(account='600563666729', region='eu-central-1'))
# PeeringStack(app, "PeeringStack",env=cdk.Environment(account='600563666729', region='eu-central-1'))
# iamusers(app, "iamusers",env=cdk.Environment(account='600563666729', region='eu-central-1'))

app.synth()
