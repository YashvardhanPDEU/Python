l = int(input("enter length: "))
b = int(input("enter breadth: "))

area = l*b
perimeter = 2*(l+b)

if area>perimeter:
    print("area is greater")
else:
    print("perimeter is greater")
