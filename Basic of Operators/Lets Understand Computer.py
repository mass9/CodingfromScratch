t = int(input()) # testcases

def decimalToBinary(n):
    count =0
    for i in range(1,n+1):
        res = n//i
        # print(res,end='')
        if res <= i :
            count+=1
    print(count)

while t>0:
    x = int(input())
    decimalToBinary(x)
    t -=1
