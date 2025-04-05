string = input("enter: ")
toggle = []
for char in string:
    if 'A' <= char <= 'Z':
        str1 = ord(char) + 32
        toggle.append(chr(str1))
    elif 'a' <= char <= 'z':
        str2 = ord(char) - 32
        toggle.append(chr(str2))

for i in toggle:
    print(i , end= "")
