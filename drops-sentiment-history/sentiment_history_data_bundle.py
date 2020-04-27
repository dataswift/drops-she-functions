import json

def lambda_handler(event, context):


    bundle = {
        "name": "sentiment-history",
        "bundle": {            		
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