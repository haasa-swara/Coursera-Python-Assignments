###Beautiful soup###
###Assignment 1- Scrapping data from HTML using Beautifulsoup###

from bs4 import BeautifulSoup
import urllib.request
total=0

sample_link = "http://py4e-data.dr-chuck.net/comments_360045.html"
fhand=urllib.request.urlopen(sample_link)
html_file = fhand.read()
soup = BeautifulSoup(html_file)
comments = soup('span') #### span is the name of the tag
for comment in comments:
   #print(comment.contents)
    num=int(comment.contents[0])
    total=total+num
print(total)