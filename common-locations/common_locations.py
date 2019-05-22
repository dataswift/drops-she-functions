
import numpy as np
from scipy.cluster.hierarchy import linkage, fcluster
from scipy.spatial.distance import pdist
import pandas as pd
import json
import sys
def parse_json(records):
    '''
    Takes in the json file containing the location data. Extracts longitude, latitude, dateCreated and dateCreated Local from each data recordself.
    Returns data.
    with open(file) as data_file:
        records = json.load(data_file)
    '''
    test = pd.io.json.json_normalize(records)  #, 'data' , ['latitude', 'longitude', 'dateCreated', 'dateCreatedLocal'],errors='ignore',)
    data = test.reindex(columns=['data.longitude','data.latitude', 'data.dateCreated', 'data.dateCreatedLocal'])
    return data


def common_locations(data,t):
    '''
    A function that takes in the location data for a single individual and
    returns the locations that they frequently visit by using aggolmerative clustering given centroid as the location.
    '''

    X = data.iloc[:,[0,1]] # Long,Lat

    # Perform agglomerative clustering using threshold t.
    dist = pdist(X, 'euclidean')
    links = linkage(dist,'single')
    #p = dendrogram(links)
    clusters = fcluster(links, t, criterion='distance')

    # Identify unique clusters and membership.
    members,counts,inds = np.unique(clusters,return_index=True, return_inverse=False, return_counts=True, axis=None)

    rankings = list(counts)

    # Output results of algorithm into dict.
    dict ={}
    for n in range(len(counts)): # for each cluster
        if inds[n]>=3: # Minium cardinality of 3 visits is currently required
            i = counts[n]
            l = inds[n]


            dict[n] = { "x": X.iloc[i:i+l,0].mean(),
                     "y": X.iloc[i:i+l,1].mean(),
                     "cardinality":l,
                     "ranking":rankings.index(i)}

    # Write results to a json file
    df = pd.DataFrame(dict)
    res = df.to_json()

    result = {
        "id": "common-locations",
        "name": "Common Locations",
        "description": "Find out which locations you visited the most and the least.",
        "summary": {
            "totalCount": len(res)
        },
        "locations": [json.loads(res)]
    }

    return [{
        "namespace": "she",
        "endpoint": "insights/common-locations",
        "data": [result],
        "linkedRecords": []
    }]


def lambda_handler(event, context):
    bundle_data = event['request']['data']['she/insights/common-locations']
    data = parse_json(bundle_data)
    return common_locations(data, 0.00095)


#with open(sys.argv[1]) as file_data:
#    data = json.load(file_data)
#    print(lambda_handler(data, None))