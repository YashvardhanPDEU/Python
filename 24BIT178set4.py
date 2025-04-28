set = {'Anil' , 'Baldev' , 'Bheem' , 'Akshay' }
listA = []
listB = []
for i in set:
    if i.startswith('A'):
        listA.append(i)
    else:
        listB.append(i)
print(listA)
print(listB)
