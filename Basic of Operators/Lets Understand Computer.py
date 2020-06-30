t = int(input()) # testcases

def decimalToBinary(n):
    if n>1:
        decimalToBinary(n//2)
    print(n%2,end='')

while t>0:
    x = int(input())
    decimalToBinary(x)
    t -=1
