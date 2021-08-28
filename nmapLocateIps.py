#!/usr/bin/python3

import os.path
import subprocess
import csv
import simplekml

arNmapResults = []
arIP = [];

if os.path.exists("ipFile.txt") == False:
  print("Error. Please create a file called ipFile.txt and supply IP Addresses separated by new line breaks.")
  exit()

ipFile = open("ipFile.txt")
for ip in ipFile:
  print("IP Address: " + ip.strip())
  args = ["nmap", "-sn", "-Pn",  "--script", "ip-geolocation-geoplugin", ip.strip()]
  p = subprocess.Popen(args, stdout=subprocess.PIPE)
  stdout, stderr = p.communicate()
  strAnswer = str(stdout, "utf-8")
  arNmapResults.append(strAnswer)
  arIP.append(ip.strip())
  #print(strAnswer)

ipCounter = 0
csvFile = open("geo-coords.csv", "w")

for lineNmap in arNmapResults:
  for line in lineNmap.split("\n"):
      if ("coordinates" in line):
        #print("COORDS:" + line)
        strCSV = arIP[ipCounter] + ',' + line.split("coordinates:")[1]
        print(strCSV)
        csvFile.write(strCSV + "\n")
        ipCounter += 1

csvFile.close()


locationFile = csv.reader(open('geo-coords.csv','r'))
kml=simplekml.Kml()

for row in locationFile:
  kml.newpoint(name=row[0], coords=[(row[2],row[1])])

kml.save('locations.kml')
