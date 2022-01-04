fname = input("Enter file name: ")
fh = open(fname)
count = 0
z = 0
for line in fh:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count +1
    y = line.find(':')
    z = z + float(line[y+1:].strip())
print('Average spam confidence:',z/count)