def lambda_handler(event, context):

    bundle = {
        "name": "busy-time",
        "bundle": {
            "calendar/google/events": {
                "endpoints": [
                    {
                        "endpoint": "calendar/google/events",
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

