print("enter dates in form of d , m , y")
date1 = []
print("enter date 1")
for i in range(1 , 4):
    x = int(input())
    date1.append(x)
print(tuple(date1))

date2 = []
print("enter date 2")
for i in range(1 , 4):
    y = int(input())
    date2.append(y)
print(tuple(date2))

if (date1[2]%4 == 0 and date1[2]%100 != 0) or (date1[2] % 400 == 0) :
    a = abs((date2[2] - date1[2])*366 + date2[2])
if (date2[2]%4 == 0 and date1[2]%100 != 0) or (date1[2] % 400 == 0) :
    a = abs((date2[2] - date1[2])*366 + date1[2])
if (date1[2]%4 == 0 and date1[2]%100 != 0) or (date1[2] % 400 == 0) and  (date2[2]%4 == 0 and date1[2]%100 != 0) or (date1[2] % 400 == 0):
    a = abs((date2[2] - date1[2])*366)
else:
    a = abs((date2[2] - date1[2])*365)
print(a)

if (date1[1] or date2[1]) == 2:
    if (date1[2]%4 == 0 and date1[2]%100 != 0) or (date1[2] % 400 == 0) and if (date2[2]%4 == 0 and date1[2]%100 != 0) or (date1[2] % 400 == 0) :
        b = abs((date1[1]-date2[1])*29)
    else:
        b = abs((date1[1]-date2[1])*28)
if (date[1] or date 
    
    
    
    




