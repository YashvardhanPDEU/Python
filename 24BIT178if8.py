x1 = int(input("enter x1: "))
y1 = int(input("enter y1: "))
x2 = int(input("enter x2: "))
y2 = int(input("enter y2: "))
x3 = int(input("enter x3: "))
y3 = int(input("enter y3: "))

a = x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)

if a == 0:
    print("points are in line")
else:
    print("not in line")
