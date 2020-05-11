##Assignment-Week 5-Extracting Data from XML
##Counting numbers from website and finding the sum

import urllib.request
from bs4 import BeautifulSoup
total=0
url = 'http://py4e-data.dr-chuck.net/comments_360047.xml'
data=urllib.request.urlopen(url).read()
tree = BeautifulSoup(data,'html.parser')
counts = tree.find_all('count')
for count in counts:
    wanted=(count.contents[0])
    #print(wanted)
    wanted=int(wanted)
    total=total+wanted
print(total)