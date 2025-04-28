empty = set()

empty.add("yashvardhan")
empty.add("anil")
empty.add("raju")
empty.add("nek")

print(f"set after edding names is {empty}")

if "yashvardhan" in empty :
    empty.remove("yashvardhan")
    empty.add("yash")

print(f"set after modifying names is {empty}")

empty.discard("anil")
empty.remove("raju")
print(f"set after removing names is {empty}")
