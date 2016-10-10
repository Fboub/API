import requests
import os
import json

api_key = os.environ[C8AE96ADAD654726AB52]
api_secret = os.environ[D86445AA3B0943748A0F7B165E7E8050]
url = 'https://api.urthecast.com/v1/consumers/apps/me/aois'

r = requests.post(https://api.urthecast.com/v1/consumers/apps/me/aois,
    headers = { 'Content-Type': 'application/json' },
    params = { 'api_key': C8AE96ADAD654726AB52, 'api_secret': D86445AA3B0943748A0F7B165E7E8050 },
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
