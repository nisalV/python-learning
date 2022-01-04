from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter a URL: ')
start = input('Start at: ')
end = input('End after: ')

i = 0
while True:
	i = i + 1
	html = urlopen(url, context = ctx).read()
	soup = BeautifulSoup(html,'html.parser')

	tags = soup('a')
	count = 0
	for tag in tags:
		count = count + 1
		if count == int(start):
			url = tag.get('href',None)
			print(i,':',url)
			continue
	if i == int(end): 
		find = re.findall('_(R.+).html',url)
		print('Last Name:',str(find[0]))
		break