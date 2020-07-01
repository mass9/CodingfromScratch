import math
t = int(input()) # testcases

#Proper approach
def decimalToBinary(n):
    i =1
    while(i <= math.sqrt(n)):
        i = i*2
        if (n//i >= i/2):
            ans = n-(n//i)
            print('i:',i)
            print('ans:',ans)
        else:
            ans = (n-(i//2)) +1
            print('ans: ',ans)
    print(ans)

# Naive approach
"""
def decimalToBinary(n):
    count =0
    for i in range(1,n+1):
        res = n//i
        # print(res,end='')
        if res <= i :
            count+=1
    print(count)
"""
while t>0:
    x = int(input())
    decimalToBinary(x)
    t -=1
