def conject(n):
    if n % 2 == 0:
        n = n/2
        conject(n)
    else:
        n = 3*n +1 
        conject(n)    
    if n == 1 :
        print('Yes')
    else:
        print('No')

t = int(input())
while t >0:
    n = int(input())
    conject(n)