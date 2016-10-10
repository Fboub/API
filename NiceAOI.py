import requests
import os
import json

api_key = os.environ[9A1B7AC1899140B2B50D]
api_secret = os.environ[F40B598E6DBB44B29FD0D71401F3F0AB]
url = 'https://api.urthecast.com/v1/consumers/apps/me/aois'

r = requests.post(https://api.urthecast.com/v1/consumers/apps/me/aois,
    headers = { 'Content-Type': 'application/json' },
    params = { 'api_key': 9A1B7AC1899140B2B50D, 'api_secret': F40B598E6DBB44B29FD0D71401F3F0AB },
    # Check out http://geojson.io for help with creating GeoJSON objects
    data = json.dumps({
        "name": "San Francisco",
        "geometry": {
            "type": "Polygon",
            "coordinates": [
                [
                    [-122.51747131347655, 37.71261539271678],
                    [-122.51747131347655, 37.82036164330873],
                    [-122.35507965087889, 37.82036164330873],
                    [-122.35507965087889, 37.71261539271678],
                    [-122.51747131347655, 37.71261539271678]
                ]
            ]
        }
    })
)

print "AOI Response:"
print json.dumps(r.json(), indent=4, separators=(',', ': '))
