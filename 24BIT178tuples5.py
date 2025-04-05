list = [(1,2,3) , () , ("hello","world") , () , (34 , "tuples") ]
new_list = []
for i in list:
    if i != ():
        new_list.append(i)

print(new_list)
