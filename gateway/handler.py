import json
import requests

def main(event, context):
    print(event)

    try:
        resp = requests.get('https://2021.pycon.kr/')

        response = {
            "statusCode": resp.status,
            "body": json.dumps(resp.data.decode('utf-8'))
        }
    except:
        response = {
            "statusCode": 500,
            "body": "Connection failed."
        }

    return response