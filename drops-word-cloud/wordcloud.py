#
# DROPS project
#
# Ming-Wei Hsu
#

import datetime
import re
from collections import Counter

def lambda_handler(event, context):
    # TODO implement
    text = ''
    #return event[1]['data']['tweets']['text'] 

    tweets = event['request']['data']['twitter/tweets']
    for row in tweets:
        if 'data' in row:
            text += row['data']['text']
    
    words = re.findall(r"\w[\w']+", text, 0)
    
    stopwords = ['https', 'all', 'just', 'being', 'over', 'both', 'through', 'yourselves', 'its', 'before', 'herself', 'had', 'should', 'to', 'only', 'under', 'ours', 'has', 'do', 'them', 'his', 'very', 'they', 'not', 'during', 'now', 'him', 'nor', 'did', 'this', 'she', 'each', 'further', 'where', 'few', 'because', 'doing', 'some', 'are', 'our', 'ourselves', 'out', 'what', 'for', 'while', 'does', 'above', 'between', 't', 'be', 'we', 'who', 'were', 'here', 'hers', 'by', 'on', 'about', 'of', 'against', 's', 'or', 'own', 'into', 'yourself', 'down', 'your', 'from', 'her', 'their', 'there', 'been', 'whom', 'too', 'themselves', 'was', 'until', 'more', 'himself', 'that', 'but', 'don', 'with', 'than', 'those', 'he', 'me', 'myself', 'these', 'up', 'will', 'below', 'can', 'theirs', 'my', 'and', 'then', 'is', 'am', 'it', 'an', 'as', 'itself', 'at', 'have', 'in', 'any', 'if', 'again', 'no', 'when', 'same', 'how', 'other', 'which', 'you', 'after', 'most', 'such', 'why', 'a', 'off', 'i', 'yours', 'so', 'the', 'having', 'once']
    
    # remove stopwords
    words = [word for word in words if word.lower() not in stopwords]
        
    # remove 's
    words = [word[:-2] if word.lower().endswith("'s") else word
                 for word in words]
    # remove numbers
    words = [word for word in words if not word.isdigit()]
    
    # convert to lowercase 
    words = [word.lower() for word in words]
    
    word_counts = Counter(words).most_common(len(words))
    
    result = {
        "id": "twitter-word-cloud",
        "name": "Twitter Word Cloud",
        "description": "This function generates a word cloud data from your twitter tweets.",
        "counts": [],
        "summary": {
            "postsAnalysed": 0,
            "totalCount": 0
        },
        "timestamp": datetime.datetime.utcnow().isoformat()
    }
    
    count_criteria = 3
    count = 0
    for w in word_counts:
        if w[1] >= count_criteria:
            result['counts'].append({"keyWord": w[0], "count": w[1]}) 
            count += w[1] 
    
    result['summary']['postsAnalysed'] = len(tweets)
    result['summary']['totalCount'] = count
    
    #return {
    #    "isBase64Encoded": False,
    #    "statusCode": 200,
    #    "headers": {
    #        "Content-Type": "application/json"
    #    },
    #    "body": json.dumps(result)
    #}

    return [{
        "namespace": "drops",
        "endpoint": "insights/twitter/word-cloud",
        "data": [result],
        "linkedRecords": []
    }]
    #return word_counts
    
    #return len(event)
    #return event[1]['endpoint']
    #return {
    #    "statusCode": 200,
    #    "body": json.dumps('Hello from Lambda!')
    #}
