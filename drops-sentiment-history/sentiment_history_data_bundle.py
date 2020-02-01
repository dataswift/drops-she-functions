import json

def lambda_handler(event, context):


    bundle = {
        "id": "sentiment_history",
        "name": "Sentiment History",
        "bundle": {
            "she/insights/emotions": {
                "endpoints": [
                    {
                        "endpoint": "she/insights/emotions",
                        "period": "daily",
                        "mapping": {
                            "source": "source", 
                            "timestamp": "timestamp"
                        }
                    }
                ],
                "orderBy": "timestamp",
                "ordering": "descending"
            }
        }
    
    };


    return json.dumps(bundle);
    
    return {
        'statusCode': 200,
        
        'context': context,
        'body': json.dumps(event)
    }