#!/usr/bin/env python3

import json
import requests
import os

quakes = requests.get("http://earthquake.usgs.gov/fdsnws/event/1/query.geojson",
                      params={
                          'starttime': "2000-01-01",
                          "maxlatitude": "58.723",
                          "minlatitude": "50.008",
                          "maxlongitude": "1.67",
                          "minlongitude": "-9.756",
                          "minmagnitude": "1",
                          "endtime": "2018-10-11",
                          "orderby": "time-asc"}
                      )

def request_map_at(lat, long, satellite=True,
                   zoom=10, size=(400, 400)):
    base = "https://static-maps.yandex.ru/1.x/?"
  
    params = dict(
        z = zoom,
        size = str(size[0]) + "," + str(size[1]),
        ll = str(long) + "," + str(lat),
        l = "sat" if satellite else "map",
        lang = "en_US"
    )

    return requests.get(base,params=params)

def map_at(*args, **kwargs):
    return request_map_at(*args, **kwargs).content


data = json.loads(quakes.text)

events = data.get('features')

magmax = 0;

for quake in events:
	mag = quake['properties']['mag']
	if mag > magmax:
		magmax = mag
		maxcoords = quake['geometry']['coordinates']

#map_response = request_map_at(maxcoords[1], maxcoords[2])
map_png = map_at(maxcoords[1],maxcoords[2]);

filename = "quake.png"
imgfile = open(filename,"wb")
imgfile.write(map_png)
imgfile.close()

os.system("feh " + filename)








