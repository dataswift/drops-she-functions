import json

def lambda_handler(event, context):


    bundle = {
        "bundle": {
            "she/insights/emotions": {
                "endpoints": [
                    {
                        "endpoint": "she/insights/emotions",
                        "mapping": {
                            "source": "source", 
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