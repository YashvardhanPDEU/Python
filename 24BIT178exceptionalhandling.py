def error_or_not():
    while True: 
        try:
            a = int(input("enter a number: "))
            print(a)
        except:
            print("invalid input")

error_or_not()
