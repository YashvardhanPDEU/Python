list1 = ["pawan kumar" , "nitin" , "payal chaudhri" , "chintan bhatt" , "vinod"]

newl = list(filter(lambda name: len(name)>8 , list1))
print(newl)
