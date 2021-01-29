import urllib.request, urllib.parse, urllib.error
import json
import ssl

url=input('enter url...')


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
try:
    js = json.loads(data)
except:
    js = None

sum=0
info =js['comments']
for item in info :
    count=item['count']
    sum=sum+count
print(sum)
