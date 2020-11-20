#!/usr/bin/env python3
import os

from aws_cdk import core

from infra_cdk.infra_cdk_stack import InfraCdkStack

REGION = os.getenv("CDK_DEFAULT_REGION", "eu-west-2")


app = core.App()
InfraCdkStack(app, "infra-cdk", env={"region": REGION})

app.synth()
