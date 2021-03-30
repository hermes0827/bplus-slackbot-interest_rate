import json
import requests
import os
from pandas import json_normalize
import read
from boto.s3.connection import S3Connection

s3 = S3Connection(os.environ['slack_token'], os.environ['channel_id'])

json_slack_path = "./token.json"
with open(json_slack_path, 'r') as json_file:
    slack_dict = json.load(json_file)

slack_token = slack_dict['token']

channel_id = slack_dict['channel_id']

message = f"""
테스트 메시지 입니다.
"""

# 파라미터
data = {'Content-Type': 'application/x-www-form-urlencoded',
        'token': slack_token,
        'channel': channel_id,
        'text': message,
        }

URL = "https://slack.com/api/chat.postMessage"
res = requests.post(URL, data=data)

print(read.read_interest_rate())

pritn(s3)
