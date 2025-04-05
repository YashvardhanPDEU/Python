# method 1

str = input("enter string: ")

vowels = ['a','e','i','o','u','A','E','I','O','U']
count = 0
i = 0
for i in range(len(str)):
    j = 0
    while j<len(vowels):
        if vowels[j] == str[i]:
            count += 1   
        j += 1    
    i += 1
print(count) 

# method 2


counta = str.count('a')
counte = str.count('e')
counti = str.count('i')
countu = str.count('u')
counto = str.count('o')

countvowel = counta + counte + counti +counto + countu
print(countvowel)
    

