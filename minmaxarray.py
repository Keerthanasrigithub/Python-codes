#finding minimum and maximum in an array
def minmax(my_arr):
    maximum=my_arr[0]
    minimum=my_arr[0]
    for i in range(1,len(my_arr)):
        if my_arr[i]>maximum:
            maximum=my_arr[i]
        if my_arr[i]<minimum:
            minimum=my_arr[i]
    return str(minimum)+ " " +str(maximum)
my_arr=list(map(int,input("enter numbers").split()))
print(minmax(my_arr))
