details = {
    1 : [ (100 , 50000) , (200 , 30000) , (300 , 20000)],
    2 : [ (400 , 15000) , (500 , 12000) , (600 , 25000)],
    3 : [ (700 , 10000) , (800 , 35000) , (900 , 40000)]
    }

for i in details:
    employee_data = details[i]
    salary = []
    for j in employee_data:
        salary.append([j[1]])
    max_salary = max(salary)
    min_salary = min(salary)

    print(f" department {i} : minimum salary is {min_salary} , maximum salary is {max_salary}")
