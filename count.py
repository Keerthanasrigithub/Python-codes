#count the number of digits in N which evenly divide N
N=int(input("enter N:"))
n=str(N)
count=0
for i in n:
    if int(i)==0:
        continue
    elif N%int(i)==0:
        count+=1
print(count)

#using fucntion
def count(N):
    n=str(N)
    count=0
    for i in n:
        if int(i)==0:
            continue
        elif N%int(i)==0:
            count+=1
    return count
N=int(input("enter N:"))
print(count(N))
            
