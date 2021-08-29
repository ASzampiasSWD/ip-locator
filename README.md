# ip-locator
This python script generates a Google Earth file from a text file of IP Addresses. The script also generates a geo-stats.csv file with information about the IPs. 
IP information includes latitude, longitude, city, region, country, ISP, and if the IP belongs to a VPN provider. 

## Steps
Install the python libraries using pip3:
<pre>
pip3 install requests
pip3 install simplekml
pip3 install csv
</pre>

Run the script

<pre>
chmod +x locateIPs.py
./locateIPs.py</pre>

## Optional VPN and ISP Detection

Steps:
<pre>
1. Register for an account on the website <a href="https://iphub.info/">https://iphub.info/</a>.
2. Generate a <b>free</b> API key. This will let you make 1000 requests a day.
3. Make a file called iphub-info.txt within the locateIPs.py directory.
4. Paste the API key in the file.
</pre>

## How-to Video
[![How To Video](https://img.youtube.com/vi/IEl-kBQvutU/0.jpg)](https://www.youtube.com/watch?v=IEl-kBQvutU)
