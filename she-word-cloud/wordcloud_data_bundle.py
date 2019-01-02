import json

def lambda_handler(event, context):

    bundle = {
        "name": "twitter-word-cloud",
        "bundle": {
            "twitter/tweets": {
                "endpoints": [
                    {
                        "endpoint": "twitter/tweets",
                        "mapping": {
                            "id": "id_str"
                        }
                    }
                ],
                "orderBy": "lastUpdated",
                "ordering": "descending"
            }
        }
    }

    return {
        "isBase64Encoded": False,
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(bundle)
    }
