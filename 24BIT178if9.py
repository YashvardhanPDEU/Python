import math

x = int(input("enter x of centre: "))
y = int(input("enter y of centre: "))
x1 = int(input("enter: "))
y1 = int(input("enter: "))
r = int(input("enter radius: "))

d = math.sqrt( (x1-x) ** 2 + (y1-y) ** 2)

if d<r:
    print("points inside circle")
elif d==r:
    print("points on circle")
else:
    print("points outside circle") 
