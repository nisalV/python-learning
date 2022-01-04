import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:

    url = input('Enter a URL: ')
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read()
    print('Retrieved', len(data), 'characters')
    print(data.decode())
    path = input('Enter tag or path: ')
    tree = ET.fromstring(data)
    results = tree.findall(path)
    print('Total counts:',len(results))

    countSum = 0
    for item in results:
        if re.match(".//.+",path):countSum += int(item.text)
        else:countSum += int(item.find('count').text)
    print('Sum:',countSum)