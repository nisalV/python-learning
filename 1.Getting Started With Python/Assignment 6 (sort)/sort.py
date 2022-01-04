while True:
	i = 0
	numbers = list()
	while i < 3:
		a = input('Enter a number:')
		b = int(a)
		numbers.append(b)
		i = i + 1
	if i == 3:
		numbers.sort()
		print(numbers)
		exit = input('Exit program [y/n]:')
		if exit == 'y':
			break
		elif exit != 'y':
			numbers.clear()
			continue
