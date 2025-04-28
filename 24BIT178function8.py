str = input("enter: ")
def convert(str):
    split = str.split()
    same = list(set(split))
    sort = sorted(same)
    final = " ".join(sort)
    print(final)
convert(str)
