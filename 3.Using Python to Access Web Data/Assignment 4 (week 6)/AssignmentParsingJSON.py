import urllib.request, urllib.parse, urllib.error
import json
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:

    url = input('Enter a URL: ')

    if len(url) < 1:break

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:js = json.loads(data)
    except:continue

    comments = js['comments']
    countSum = 0 
    count = 0
    for comment in comments:
        count += 1
        countSum += int(comment['count'])
    print('Comment count:',count)
    print('Sum:',countSum)