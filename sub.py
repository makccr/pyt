#!/usr/bin/env python

import urllib.request
import json

USERNAME="YOUTUBE-USERNAME" #replace with channel username

# You can also need to update the filepath below, with the path to a text document
# containing your YouTube API key.
# Default: /home/YOURSYSTEMUSERNAME/.config/polybar/api.txt
with open("PATH TO API.TXT", "r") as file:
    APIKEY = file.readline().strip()

data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername="+USERNAME+"&key="+APIKEY).read()
subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]

print("{:,d}".format(int(subs)))
