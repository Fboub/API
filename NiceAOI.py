import requests
import os
import json

api_key = os.environ[5D53384399C247A8B62E]
api_secret = os.environ[6688A17B274149CAA87FCF56FCFCFAD7]
url = 'https://api.urthecast.com/v1/consumers/apps/me/aois'

r = requests.post(https://api.urthecast.com/v1/consumers/apps/me/aois,
    headers = { 'Content-Type': 'application/json' },
    params = { 'api_key': 5D53384399C247A8B62E, 'api_secret': 6688A17B274149CAA87FCF56FCFCFAD7 },
    # Check out http://geojson.io for help with creating GeoJSON objects
    data = json.dumps({
        "name": "NICE",
        "geometry": {
            "type": "Polygon",
            "coordinates": [
          [
            [
              7.181625366210937,
              43.689970160120666
            ],
            [
              7.225570678710937,
              43.72049745570917
            ],
            [
              7.299728393554687,
              43.726700289570324
            ],
            [
              7.332344055175781,
              43.710075249008575
            ],
            [
              7.355003356933594,
              43.68624625567728
            ],
            [
              7.341613769531249,
              43.667871610117494
            ],
            [
              7.241020202636719,
              43.65470793293131
            ],
            [
              7.200508117675782,
              43.63781445968477
            ],
            [
              7.1706390380859375,
              43.64725551568439
            ],
            [
              7.181625366210937,
              43.689970160120666
            ]
          ]
        ]
      }
    }

print "AOI Response:"
print json.dumps(r.json(), indent=4, separators=(',', ': '))
