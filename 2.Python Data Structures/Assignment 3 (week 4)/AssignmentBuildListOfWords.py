fname = input("Enter file name: ")
fh = open(fname)
lst = list()
element = 0
element = 0
for line in fh:
    line = line.rstrip()
    words = line.split()
    for element in words:
        if element not in lst:
            lst.append(element)
lst.sort()
print(lst)
