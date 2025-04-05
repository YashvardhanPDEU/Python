string = input("enter: ")
upper = []
for char in string:
    if 'a' <= char <= 'z' :
        str = ord(char) - 32
        upper.append(chr(str))
    else:
        upper.append(char)

for i in upper:
    print(i , end="")
    
