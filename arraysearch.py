#search an element in an array
def find(my_arr,x):
    for i in my_arr:
        if my_arr[i]==x:
            return i
my_arr=list(map(int,input("enter numbers in an array:").split()))
x=int(input("enter the number:"))
print(find(my_arr,x))
