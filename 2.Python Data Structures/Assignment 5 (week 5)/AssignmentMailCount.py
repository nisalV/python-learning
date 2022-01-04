name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counts = dict()

for line in handle:
    if line.startswith('From '):
        words = line.split()
        counts[words[1]] = counts.get(words[1],0) + 1
bigCount = None
bigWord = None

for word,count in counts.items():
    if bigCount is None or count > bigCount:
        bigCount = count
        bigWord = word
print(bigWord,bigCount)