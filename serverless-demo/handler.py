import json
import requests

def hello(event, context):
    temp = requests.get('https://2021.pycon.kr/')

    body = {
        "message": temp.text
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    