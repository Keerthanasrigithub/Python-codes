#find missing in array
def find(my_arr,n):
    for i in range(1,n+1):
        if i not in my_arr:
            return i
my_arr=list(map(int,input("enter numbers in array:").split()))
n=int(input("enter number:"))
print(find(my_arr,n))
