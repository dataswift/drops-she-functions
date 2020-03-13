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
                            "text": "text",
                            "lastUpdated": "lastUpdated"
                        }
                    }
                ],
                "orderBy": "lastUpdated",
                "ordering": "descending",
                "limit": 100
            }
        }
    }

    return bundle
    #return {
    #    "isBase64Encoded": False,
    #    "statusCode": 200,
    #    "headers": {
    #        "Content-Type": "application/json"
    #    },
    #    "body": json.dumps(bundle)
    #}
