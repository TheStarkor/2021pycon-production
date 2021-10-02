import json


def hello(event, context):
    body = {
        "message": "Welcome to pycon2021",
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """

def pycon(event, context):
    # excel
    # ...

    return {"result": 123}