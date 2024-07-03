#find palindrome or not..if it is palindrome return yes else return no
def palindrome(n):
    x=str(n)
    y=list()
    for i in x:
        num=int(i)
        y.append(num)
    palindrome1=y.copy()    
    palindrome1.reverse()
    int_result=int(''.join(map(str,palindrome1)))
    if int_result==n:
        return "Yes"
    else:
        return "No"
n=int(input("enter n:"))
print(palindrome(n))
