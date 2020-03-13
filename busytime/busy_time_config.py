#
# DROPS project
#
# Ming-Wei Hsu
#
def lambda_handler(event, context):
    # TODO implement
    
    config = {
        "id": "busy-time",
        "info": {
            "version": "1.0.0",
            "versionReleaseDate": "2019-09-03T12:00:00.000Z",
            "name": "Busy Time",
            "headline": "Analysis of your busy time ",
            "description": {
                "text": "You can see the analysis of your meetings on Google calendar. "
            },
            "termsUrl": "https://hatdex.org/terms-of-service-hat-owner-agreement",
            "supportContact": "m.hsu@surrey.ac.uk",
            "graphics": {
                "banner": {
                    "normal": ""
                },
                "logo": {
                    "normal": "https://github.com/Hub-of-all-Things/exchange-assets/blob/master/wordcloud/logo.png?raw=true"
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
            "dataPreviewEndpoint": "/she/feed/drops/busy-time"
        },
        "developer": {
            "id": "drops",
            "name": "DROPS project",
            "url": "https://www.hatcommunity.org/about-drops/",
            "country": "United Kingdom"
        },
        "trigger": {
            "period": "P1D",
            "triggerType": "periodic"
        },
        "dataBundle": {
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
        },
        "status": {
            "available": True,
            "enabled": False
        }
    }

    return config

