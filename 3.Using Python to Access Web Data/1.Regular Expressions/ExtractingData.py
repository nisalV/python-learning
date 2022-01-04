import re
x = 'My 2 for 43 with 19 My You'
y = re.findall('[0-9]+',x) # findall: get a list of all possible matches.
print(y) # ['2','43','19']

y = re.findall('[MYA]+',x) # find one or more 'M','Y','A'. plus means greater than one.
print(y) # ['M','M','Y']

p = 'From: you : to'
q = re.findall('^F.+:',p) # '^'- frist character, '.'- last character, '+'- has one or more characters.
print(q) # ['From: you :'] ** we want 'From:' but get 'From: you :'. this is greedy matching.

q = re.findall('^F.+?:',p) # '?'- don't be greedy.
print(q) # ['From:']

r = 'From nisal@gmail.com Sat Jan 5 09:12 2008'
s = re.findall('\S+@\S+',r) # '\S+'- atleast one or more non-whitespace characters.
print(s) # ['nisal@gmail.com']

s = re.findall('^From (\S+@\S+)',r) # check if the line starts from 'From' and then extracts whats in the ().
print(s) # ['nisal@gmail.com']

s = re.findall('@([^ ]*)',r) # find '@' but return all characters without blank after that [^ ]
print(s) # ['gmail.com']

s = re.findall('^From .*@([^ ]*)',r) # starts with 'From ' ad any number of characters upto '@' and extract....
print(s) # ['gmail.com']
