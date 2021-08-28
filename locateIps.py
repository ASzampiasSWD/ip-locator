#!/usr/bin/python3

import os.path
import requests
import json
import subprocess
import csv
import simplekml

arGeoResults = []

if os.path.exists("ipFile.txt") == False:
  print("Error. Please create a file called ipFile.txt and supply IP Addresses separated by new line breaks.")
  exit()

ipFile = open("ipFile.txt")
for ip in ipFile:
  print("IP Address: " + ip.strip())
  response = requests.get("http://www.geoplugin.net/json.gp?ip=" + ip)
  strResponse = response.content.decode("utf-8")
  jsonResponse = json.loads(strResponse)
  if (response.status_code == 200):
    arGeoResults.append(jsonResponse)
  else:
    print(ip + " had an error. Status Code " + response.status_code)

geoFile = open("geo-coords.csv", "w")
statsFile = open("geo-stats.csv", "w")
strStatsTitle = "IP Address, Latitude, Longitude, City, Region, Country, Timezone\n"
statsFile.write(strStatsTitle)

for jsonGeo in arGeoResults:
  strGeoTitle = '"' + jsonGeo["geoplugin_request"].strip() + ' ' + jsonGeo["geoplugin_city"] + '"';
  strGeo = strGeoTitle + ',' + jsonGeo["geoplugin_latitude"] + ',' + jsonGeo["geoplugin_longitude"]    
  strStats = jsonGeo["geoplugin_request"].strip() + ',' + jsonGeo["geoplugin_latitude"] + ',' + jsonGeo["geoplugin_longitude"] + ',' + \
             jsonGeo["geoplugin_city"] + ',' + jsonGeo["geoplugin_region"] + ',' + jsonGeo['geoplugin_countryName'] + ',' + \
             jsonGeo["geoplugin_timezone"]
  print(strGeo)
  geoFile.write(strGeo + "\n")
  statsFile.write(strStats + "\n")

geoFile.close()
statsFile.close()

locationFile = csv.reader(open('geo-coords.csv','r'))
kml=simplekml.Kml()

for row in locationFile:
  kml.newpoint(name=row[0], coords=[(row[2],row[1])])

kml.save('locations.kml')
print("Success! locations.xml and geo-status.csv have been created.")
