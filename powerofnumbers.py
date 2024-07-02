#power of numbers-Given a no...Find its reverse and find that number is raised to the power of its own reverse
#as answers can be very large,print the resul 10^9+7

N=int(input("enter N:"))
R=0
original=N
while N>0:
    digit=N%10
    R=R*10+digit
    N=N//10
power=original**R
result=power%((10**9)+7)
print(result)
