import json

data = '''{
	"name" : "Nisal",
	"phone" : {
		"type" : "intl",
		"number" : "+94 71 256 2035"
		},
	"email" : {
		 "hide" : "yes"
	}
}'''

info = json.loads(data) # info is a dictionary
print('Name:',info["name"]) # since info is a dictionary, ["name"] is a key
print('Phone:',info["phone"])
print('Email:',info["email"]["hide"])

data2 = '''[
	{	"id" : "001",
		"x" : "2",
		"name" : "Nisal"
	},
	{	"id" : "009",
		"x" : "7",
		"name" : "Pathmila"
	}
]''' # in a sense, this is a list with 2 dictionaries as elements

info = json.loads(data2) # this time, info is a list
print('User count', len(info))
for item in info:
	print('Name:', item['name'])
	print('Id:',item['id'])
	print('Attribute',item['x'])