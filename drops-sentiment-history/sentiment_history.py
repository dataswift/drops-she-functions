from datetime import datetime
from dateutil import tz

def lambda_handler(event, context):

    #return event[1]['data']['text'] 
    #t = event[1]['data']['timestamp']
    #date = datetime.strptime(t, '%Y-%m-%dT%H:%M:%S.%fZ')
    #return date.isoformat() 
    
    # sentiment of all sources and periods, length-weighted average 
    st = dict()
    textlen = dict() 
    #text = ''

    insights = event['request']['data']['she/insights/emotions']
    for row in insights:
        if 'data' in row:
            record = row['data']
            if 'text' in record and 'source' in record and 'sentiment' in record and 'timestamp' in record:
                length = len(record['text']) 
                date = datetime.strptime(record['timestamp'], '%Y-%m-%dT%H:%M:%S.%fZ')
                start = datetime(date.year, date.month, date.day, tzinfo=tz.tzutc())
                
                score = 0 
                sentiment = record['sentiment'] 
                
                if sentiment == 'Very Negative':
                    score = -2 
                elif sentiment == 'Negative':
                    score = -1 
                elif sentiment == 'Positive':
                    score = 1
                elif sentiment == 'Very Positive':
                    score = 2  
                    
                source = record['source']
                if source not in st:
                    st[source] = dict()
                    textlen[source] = dict() 
                
                if start.isoformat() not in st[source]:
                    st[source][start.isoformat()] = score
                    textlen[source][start.isoformat()] = length
                else:
                    st[source][start.isoformat()] = (score * length + st[source][start.isoformat()] * textlen[source][start.isoformat()]) / (length + textlen[source][start.isoformat()])
                    textlen[source][start.isoformat()] += length

    total = 0
    for source in st:
        total += len(source)
        
    result = {
        "id": "sentiment-history",
        "name": "Sentiment History",
        "description": "This function generates the sentiment of the text in the past.",
        "summary": {
            "sources": 0,
            "totalCount": 0
        },
        "data": []
    }

    result['summary']['sources'] = len(st)
    result['summary']['totalCount'] = total
    result["data"] = st

    return [{
        "namespace": "drops",
        "endpoint": "insights/sentiment-history",
        "data": [result],
        "linkedRecords": []
    }]
