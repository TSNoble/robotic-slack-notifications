import yaml
from pathlib import Path

from aws_cdk import (
    Stack,
    aws_sns as sns,
    aws_lambda as lambda_,
    aws_lambda_python_alpha as lambda_python,
    aws_lambda_event_sources as event_sources,
)

from constructs import Construct

class RosSlackbotStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        ros_msg_topic = sns.Topic(self, "RosMessages")
        with open(Path.cwd().parent/".credentials/slack.yaml", "r") as credentials_file:
            credentials = yaml.load(credentials_file)
        ros_slackbot = lambda_python.PythonFunction(
            self,
            id="my-function",
            entry=str(Path.cwd().parent/"slack"),
            runtime=lambda_.Runtime.PYTHON_3_9,
            index="ros_slackbot.py",
            handler="handler",
            environment=credentials
        )
        ros_slackbot.add_event_source(
            event_sources.SnsEventSource(ros_msg_topic)
        )