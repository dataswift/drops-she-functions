def lambda_handler(event, context):

    bundle = {
        "name": "sentiment-history",
        "bundle": {
            "she/insights/emotions": {
                "endpoints": [
                    {
                        "endpoint": "she/insights/emotions",
                        "mapping": {
                            "id": "id_str"
                        }
                    }
                ],
                "orderBy": "timestamp",
                "ordering": "descending",
                "limit": 1000
            }
        }
    
    }

    return bundle
