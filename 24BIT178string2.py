string = input("enter string: ")
lower = []
for char in string:
    if 'A' <= char <= 'Z':
        str = ord(char) + 32
        lower.append(chr(str))
    else:
        lower.append(char)

for i in lower:
    print(i, end="")
        
        
