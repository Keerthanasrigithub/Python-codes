#find perfect number
def perfect_num(n):
    perfect=list()
    sum=0
    for i in range(1,n+1):
        if n%i==0:
            perfect.append(i)
    perfect.remove(n)
    for i in perfect:
        sum=sum+i
    if sum==n:
        return 1
    else:
        return 0
n=int(input("enter n:"))
print(perfect_num(n))
