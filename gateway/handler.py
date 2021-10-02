import json
import requests

def main(event, context):
    print(event)

    try:
        resp = requests.get('https://2021.pycon.kr/')

        response = {
            "statusCode": resp.status_code,
            "body": resp.text
        }
        
    except:
        response = {
            "statusCode": 500,
            "body": "Connection failed."
        }

    return response