str1 = input("enter first: ")
str2 = input("enter second: ")
if str1.count(str2) == True:
    print("str2 is in str1")
elif str2.count(str1) == True:
    print("str1 is in str2")
else:
    print("both string are different")
