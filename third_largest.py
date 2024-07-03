#find third largest element in an array
def third_largest(my_arr):
    first=second=third=float('-inf')
    for num in my_arr:
        if num>first:
            third=second
            second=first
            first=num
        elif num>second and num!=first:
            third=second
            second=num
        elif num>third and num!=second and num!=first:
            third=num
    return third
my_arr=list(map(int,input("enter the numbers:").split()))
print(third_largest(my_arr))
