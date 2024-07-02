#find prime or not

def prime(n):
    if n>1:
        for i in range(2,(n//2)+1):
            if n%i==0:
                return 0
        return 1    
    else:
        return 0
n=int(input("enter n:"))
print(prime(n))
