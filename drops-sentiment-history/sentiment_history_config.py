#
# DROPS project
#
# Ming-Wei Hsu
#
def lambda_handler(event, context):
    
    config = {
        "id": "sentiment-history",
        "info": {
            "version": "1.0.0",
            "versionReleaseDate": "2019-03-08T12:00:00.000Z",
            "name": "Sentiment History",
            "headline": "History of your sentiment",
            "description": {
                "text": "Sentiment history generates the history of your sentiment from your tweets and facebook feeds "
            },
            "termsUrl": "https://hatdex.org/terms-of-service-hat-owner-agreement",
            "supportContact": "Ming-Wei.Hsu@uwe.ac.uk",
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
            "dataPreviewEndpoint": "/she/feed/drops/sentiment-history"
        },
        "developer": {
            "id": "drops",
            "name": "DROPS project",
            "url": "https://www.hatcommunity.org/about-drops/",
            "country": "United Kingdom"
        },
        "trigger": {
            "period": "P1W",
            "triggerType": "periodic"
        },
        "dataBundle": {
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
        },
        "status": {
            "available": True,
            "enabled": False
        }
    }

    return config
