str = input("enter sentence: ")

def count_lower_upper(str):
    lower = 0
    upper = 0
    for i in str:
        if i.islower():
            lower += 1
        if i.isupper():
            upper += 1
    dict = {
        "upper": upper ,
        "lower": lower

    }
    print(dict)


count_lower_upper(str)
    
        
