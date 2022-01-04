hrs = input("Enter Hours:")
h = float(hrs)

rate = input("Enter rate:")
r = float(rate)

if h <= 40 and h >= 0:
    pay = h*r
if h > 40:
    pay = (40*r + (h-40)*r*1.5)
print(pay)