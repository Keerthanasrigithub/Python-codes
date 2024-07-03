#sort 0s,1s and 2s inn an array
def sorting(my_arr):
    low=0
    mid=0
    high=len(my_arr)-1
    while mid<=high:
        if my_arr[mid]==0:
            my_arr[low],my_arr[mid]=my_arr[mid],my_arr[low]
            low+=1
            mid+=1
        elif my_arr[mid]==1:
            mid+=1
        elif my_arr[mid]==2:
            my_arr[mid],my_arr[high]=my_arr[high],my_arr[mid]
            high-=1
    return my_arr        
my_arr=list(map(int,input("enter").split()))
sorted=sorting(my_arr)
int_result=(' '.join(map(str,sorted)))
print(int_result)
            
