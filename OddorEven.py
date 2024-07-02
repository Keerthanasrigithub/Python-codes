#find the given number is odd or even

def oddeven(n):
    if n%2==0:
        return "even"
    else:
        return "odd"

n=int(input("enter n:"))
print(oddeven(n))
