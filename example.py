import json
import requests

def get_jobs(skills):

    endpoint='http://dev-ng-search.phenompeople.com/search/refine'
    data=json.dumps({
        "keywords":'python',
        "counts":False,
        "jobs":True,
        "parentRefNum":"DELOA003X",
        "global":True,
        "locale":"en_US",
        "selected_fields":{},
        "all_fields":["category"],
        "refNum":"DELOA003X",
        "size":5,
        "requestID":"temp",
        "supportLang":"en_US",
        "from":0
    })
    r = requests.post(endpoint, data=data,headers={'Content-type': 'application/json'})
    print r.status_code
    x = r.json()
    print x
    print x['status']
    print x.keys()
    print x['totalHits']
    print type(x['hits'])
    print type(x['data'])
    print type(x['eid'])
    print x['data'].keys()
    print type(x['data']['jobs'])
    print len(x['data']['jobs'])
    print x['data']['jobs'][0]
    print type(x['data']['jobs'][0])
    print len(x['data']['jobs'][0])
    print x['data']['jobs'][0].keys()
    print x['data']['jobs'][0]['type']
    print x['data']['jobs'][0]['category']

    for i in x['data']['jobs']:
        print i['title']
        print i['type']
        print i['category']

    if r.status_code != requests.codes.ok:
        print r.text


get_jobs('python')


"""
    print x['data']['jobs'][1]
    print type(x['data']['jobs'][1])
    print len(x['data']['jobs'][1])
    print x['data']['jobs'][2]
    print type(x['data']['jobs'][2])
    print len(x['data']['jobs'][2])
    print x['data']['jobs'][3]
    print type(x['data']['jobs'][3])
    print len(x['data']['jobs'][3])
    print x['data']['jobs'][4]
    print type(x['data']['jobs'][4])
    print len(x['data']['jobs'][4])
  """