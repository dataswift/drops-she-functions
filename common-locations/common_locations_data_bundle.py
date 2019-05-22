def lambda_handler(event, context):

    bundle = {
        "name": "common-locations",
        "bundle": {
            "she/insights/common-locations": {
                "endpoints": [
                    {
                        "endpoint": "rumpel/locations/ios"
                    },
                    {
                        "endpoint": "rumpel/locations/android"
                    }
                ],
                "orderBy": "dateCreated",
                "ordering": "descending",
                "limit": 1000
            }
        }
    
    }

    return bundle
