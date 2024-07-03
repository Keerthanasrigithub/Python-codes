#find squar root of a number
import math
def floorsqrt(n):
    sq_root=math.sqrt(n)
    round_sq_root=round(sq_root)
    return round_sq_root
n=int(input("enter the number:"))
print(floorsqrt(n))
