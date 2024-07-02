#gcd of two numbers

def gcd(a,b):
    while b != 0:
        c=a%b
        a=b
        b=c
    return a
a=int(input("enter a:"))
b=int(input("enter b:"))
print(gcd(a,b))

#in order to find gcd of three numbers

def gcd(a,b):
    while b != 0:
        d=a%b
        a=b
        b=d
    return a
a=int(input("enter a:"))
b=int(input("enter b:"))
c=int(input("enter c:"))
gcd_ab=gcd(a,b)
gcd_abc=gcd(gcd_ab,c)
print("The gcd of three numbers is",gcd_abc)


