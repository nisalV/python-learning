smallest = None # flag
i = 0
print('before',smallest)
for value in [3,41,12,9,74,15]:
    if smallest is None:
        smallest = value
    elif smallest > value:
        smallest = value
    print(smallest,value)
print('after',smallest)
