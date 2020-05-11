##Week 6 Assignment-1
#Extracting Data from JSON

import urllib.request
import json
count=0
url=' http://py4e-data.dr-chuck.net/comments_360048.json'
fh=urllib.request.urlopen(url)
file=fh.read()
#print(file)
data=json.loads(file)
for d in data['comments']:
    #print(d['count'])
    count=count+(d['count'])
print(count)