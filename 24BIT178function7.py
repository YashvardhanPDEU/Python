A = input("enter name: ")
def palindrome(A):
    i = 0
    for i in range(len(A)//2):
        if A[i]==A[len(A)-i-1]:
            print("palindrome")
        else:
            print("no")
palindrome(A)
