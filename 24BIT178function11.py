first = int(input("enter length of list1: "))
second = int(input("enter length of list2: "))
def create_list(first,second):
    list1 = []
    list2 = []
    for i in range(first):
                 x = int(input())
                 list1.append(x)
    print(list1)            

    for i in range(second):
                 y = int(input())
                 list2.append(y)
    print(list2)             

    list1.extend(list2)
    print(list1)

create_list(first,second)    
