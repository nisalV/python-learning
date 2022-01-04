# I'm calculating the sum of numbers in both 'sample data' and 'actual data' file.
import re
FileList = ['regex_sum_42.txt','regex_sum_1421969.txt']

for item in FileList:
	hand = open(item)
	numSum = 0
	for line in hand:
		line = line.strip()
		numList = re.findall('[0-9]+',line)
		if len(numList) > 0:
			for element in numList:
				numSum = numSum + int(element)
		else: continue
	print('Sum of the numbers in',item,':',numSum)