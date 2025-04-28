lst = ['madam','Python',"malayalam",12321]

palindrome = list(filter(lambda item: str(item) == str(item)[ :: -1 ] , lst))

print(palindrome)

   
