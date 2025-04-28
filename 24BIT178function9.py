str = input("enter string: ")
def count_alpha_digits(str):
    alphabets = 0
    digits = 0
    for i in str:
        if i.isalpha():
            alphabets += 1
        if i.isnumeric():
            digits += 1
                        
    dict = {
        'alphabets' : alphabets ,
        'digits' : digits
        }
    print(dict)
  
    

count_alpha_digits(str)
    
