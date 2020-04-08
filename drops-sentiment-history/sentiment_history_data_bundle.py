import json

def lambda_handler(event, context):


    bundle = {
        "bundle": {
            "name": "sentiment-history",		
            "she/insights/emotions": {
                "endpoints": [
                    {
                        "endpoint": "she/insights/emotions",
                        "mapping": {
                            "source": "source", 
                            "text": "text",
                            "sentiment": "sentiment",
                            "timestamp": "timestamp"
                        }
                    }
                ],
                "orderBy": "timestamp",
                "ordering": "descending",
				"limit": 100
            }
        }
    
    }


    return bundle   