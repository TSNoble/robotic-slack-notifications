#!/usr/bin/python3

import rospy
import rostopic
import boto3
from rospy_message_converter import json_message_converter


class AwsPublisher:

    def __init__(self, sns_topic, ros_topic):
        self._sns_topic = sns_topic
        topic_type, _, _ = rostopic.get_topic_class(ros_topic)
        self._subscriber = rospy.Subscriber(ros_topic, topic_type, self._send_to_sns)

    def _send_to_sns(self, message):
        self._sns_topic.publish(Message=json_message_converter.convert_ros_message_to_json(message))


if __name__ == "__main__":
    rospy.init_node("aws_publisher")
    sns = boto3.resource("sns")
    sns_topic = sns.Topic("arn:aws:sns:eu-west-2:778015471639:RosSlackbotStack-RosMessagesAE9B8EEF-GU9WalgK1XBT")
    ros_topic = "/move_group/result"
    _ = AwsPublisher(sns_topic, ros_topic)
    rospy.spin()