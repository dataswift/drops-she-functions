import json
import base64
def hello(event, context):
    response = {
        "statusCode": 200,
        "body": event['body']
    }

    return response

