#!/usr/bin/env python3
import os


import aws_cdk as cdk

from hello_cdk.hello_cdk_stack import HelloCdkStack


app = cdk.App()
HelloCdkStack(app, "HelloCdkStack", env=cdk.Environment(account='600563666729', region='eu-central-1'))
app.synth()
