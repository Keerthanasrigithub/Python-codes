N=int(input("enter"))
reversed=0
count=list()
while N>0:
    digit=N%10
    reversed=reversed*10+digit
    N=N//10
print(reversed)
x=str(reversed)
for i in x:
    if int(i)==0:
        continue
    elif int(i)!=0:
        count.append(int(i))
int_result=int(''.join(map(str,count)))
print("result",int_result)
