largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    else:
        
        try:
            n = float(num)
            if smallest is None:
                smallest = n
            if largest is None and smallest < n:
                largest = n
            elif smallest > n:
                smallest = n
        except:
            print('Invalid input')

print("Maximum is", int(largest))
print("Minimum is", int(smallest))