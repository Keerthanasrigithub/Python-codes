#find the last digit of a^b for large numbers

def getlastdigit(a,b):
    c=a**b
    d=c%10
    return d
a=int(input("enter a:"))
b=int(input("enter b:"))
print(getlastdigit(a,b))
