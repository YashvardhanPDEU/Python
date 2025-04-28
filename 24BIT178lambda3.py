import random

random.numbers = random.sample(range(-15,16) , 10)

newl = list(map(lambda x: x*x , random.numbers))

print("original list : ",random.numbers)
print("squared list : " , newl)
