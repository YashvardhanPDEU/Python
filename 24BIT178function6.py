end = int(input("enter ending value: "))

def list_tuple_series(end_value):
    lst = []
    for i in range(1,end+1):
        list = [i,i**2,i**3]
        tup = tuple(list)
        lst.append(tup)
    print(lst)   
        
list_tuple_series(end)
    
    
    
