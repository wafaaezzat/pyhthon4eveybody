
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
counts=input('enter counts')
position=input('enter position')
count=int(counts)+1
pos=int(position)

lst1=list()
for i in range(0,count):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
        needed_tags=tag.get('href', None)
        lst1.append(needed_tags)
        url=lst1[pos]
    print(url)
