import xml.etree.ElementTree as ET
data = '''<person>
	<name>Nisal</name>
	<phone type="intl">
		+94 71 256 2035
	</phone>
	<email hide="yes"/>
	</person>'''         # ''' will include 'new line \n' at the end of each line of the 'data'.

tree = ET.fromstring(data) # take the string and give a nice data tree (tree of information)!
print('Name:',tree.find('name').text)  # find the tag 'name' get the information in tag.
print('Attr:',tree.find('email').get('hide')) # to get the atribute 'hide' returns "yes".

input = '''<stuff>
	<users>
		<user x="2">
			<id>001</id>
			<name>Nisal</name>
		</user>
		<user x="7">
			<id>009</id>
			<name>Pathmila</name>
		</user>
	</users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count:',len(lst))
print(lst)
for item in lst:
	print('Name:', item.find('name').text)
	print('Id:', item.find('id').text)
	print('Attrbute:',item.get("x"))
