import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl



url =input('Enter __')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
counts=input('enter counts: ')
position=input('enter position: ')
all_num_list = list()
link_position = 18
Process_repeat = 7


print("Retrieving:",url)
tags = soup('a')
for i in range(0,Process_repeat):
    target = tags[link_position - 1]
    url = target.get('href', None)
    print("Retrieving:", url)
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
