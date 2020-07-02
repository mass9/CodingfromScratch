def conject(n):
    while True:
        if n % 2 == 0:
            n = n//2
            if (n==1):
                print('YES')
                break
        else:
            n = 3*n +1 
            if (n==1):
                print('YES')
                break     

t = int(input())
while t >0:
    n = int(input())
    conject(n)