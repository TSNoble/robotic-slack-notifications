import os
import json
from slack_sdk import WebClient
from slack_sdk.models.blocks import Block

client = WebClient(token=os.environ["SLACK_BOT_TOKEN"])
success = "🟢 Motion Succeeded"
failure = "🔴 Motion Failed"

def parse_motion_result(result):
    header = {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": success if result["result"]["error_code"]["val"] == 1 else failure,
            "emoji": True
        }
    }
    text = {
        "type": "section",
        "text": {
            "type": "plain_text",
            "text": result["status"]["text"]
        }
    }
    return Block.parse_all([header, text])


def handler(event, _):
    message = event['Records'][0]['Sns']['Message']
    client.chat_postMessage(channel="#random", blocks=parse_motion_result(json.loads(message)))
