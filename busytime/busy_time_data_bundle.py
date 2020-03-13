def lambda_handler(event, context):

    bundle = {
        "name": "busy-time",
        "bundle": {
            "calendar/google/events": {
                "endpoints": [
                    {
                        "endpoint": "calendar/google/events",
                        "mapping": {
                            "created": "created",
							"status": "status",
							"start": "start",
							"end": "end"
                        }
                    }
                ],
                "orderBy": "created",
                "ordering": "descending",
                "limit": 100
            }
        }
    
    }

    return bundle

