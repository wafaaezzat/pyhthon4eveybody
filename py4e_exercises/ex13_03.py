import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = '  http://py4e-data.dr-chuck.net/comments_476568.xml'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
sum=0
while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)
    print('Retrieving', url)

    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read()

    tree = ET.fromstring(data)
    #print(tree)
    #print(data)
    lst = tree.findall('comments/comment')
    for item in lst:
        number=item.find('count').text
        sum=int(number)+sum
    print(sum)
