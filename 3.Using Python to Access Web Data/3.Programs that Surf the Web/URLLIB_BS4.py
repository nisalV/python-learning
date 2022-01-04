import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter : ')

html = urllib.request.urlopen(url, context = ctx).read() # read all in url

soup = BeautifulSoup(html,'html.parser')

tags = soup('span') # go through all the '<a>' tags and give list of them, [..,..,..]

numCount = 0
count = 0
for tag in tags:
	numCount = numCount + 1
	count = count + int(tag.contents[0])
	# print('TAG:', tag)
    # print('URL:', tag.get('href', None))
    # print('Contents:', tag.contents[0])
    # print('Attrs:', tag.attrs)
print('Number Count:',numCount)
print('SUM:',count)