import math
t = int(input())
for _ in range(t):
    a,b,c = [int(x) for x in input().split()]
    res = (2*b) -(a+c)
    if res == 0:
        pass
    else:
        res = math.ceil(abs((2*b)-(a+c))/2)
    print(res)