def calc_series(n):
    a = n + (n*10+n) + (n*100+n*10+n) + (n*1000+n*100+n*10+n)
    print(a)

number = int(input("enter number: "))
calc_series(number)  
