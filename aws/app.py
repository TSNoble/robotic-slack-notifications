#!/usr/bin/env python3

import aws_cdk as cdk

from ros_slackbot_stack import RosSlackbotStack

app = cdk.App()
RosSlackbotStack(app, "RosSlackbotStack")
app.synth()
