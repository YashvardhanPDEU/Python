maths = int(input("enter mark1: "))
science= int(input("enter mark2: "))
english = int(input("enter mark3: "))
hindi = int(input("enter mark4: "))
social = int(input("enter mark5: "))

def sum_avg(a,b,c,d,e):
    sum = a+b+c+d+e
    average = (a+b+c+d+e)/5

    print(f"sum is {sum}")
    print(f"average is {average}")

sum_avg(maths,science,english,hindi,social)
