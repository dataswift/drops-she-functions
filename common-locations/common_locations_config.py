#
# DROPS project
#
# Ming-Wei Hsu
#
def lambda_handler(event, context):
    # TODO implement
    
    config = {
        "id": "common-locations",
        "info": {
            "version": "1.0.0",
            "versionReleaseDate": "2019-05-01T12:00:00.000Z",
            "name": "Common Locations",
            "headline": "Find out which locations you visited the most and the least.",
            "description": {
                "text": "Common Locations takes an individual's location data for a given period and identifies the locations that they have frequently visited."
            },
            "termsUrl": "https://hatdex.org/terms-of-service-hat-owner-agreement",
            "supportContact": "Z.Wood@greenwich.ac.uk",
            "graphics": {
                "banner": {
                    "normal": ""
                },
                "logo": {
                    "normal": "https://github.com/Hub-of-all-Things/exchange-assets/blob/master/common-locations/logo.png?raw=true"
                },
                "screenshots": [
                    {
                        "normal": ""
                    },
                    {
                        "normal": ""
                    }
                ]
            },
            "dataPreviewEndpoint": "/she/feed/insights/common-locations"
        },
        "developer": {
            "id": "greenwich",
            "name": "University of Greenwich",
            "url": "https://www.gre.ac.uk/",
            "country": "United Kingdom"
        },
        "trigger": {
            "period": "P1W",
            "triggerType": "periodic"
        },
        "dataBundle": {
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
        },
        "status": {
            "available": True,
            "enabled": False
        }
    }

    return config
