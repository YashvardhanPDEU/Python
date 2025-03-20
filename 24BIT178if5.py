first = int(input("enter first angle: "))
second = int(input("enter second angle: "))
third = int(input("enter third angle: "))

if first == 0:
    print("not a triangle")
if second == 0:
    print("not a triangle")
if third == 0:
    print("not a triangle")
if first+second+third == 180 :
    print("perfect triangle")
else:
    print("not perfect triangle")
