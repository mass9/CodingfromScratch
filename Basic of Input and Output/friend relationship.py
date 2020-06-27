t = int(input()) # number of testcases
for _ in range(t):
    n = int(input())
    for i in range(1,n+1):
        s= '*'*i
        h = '#'*((n-i)*2)
        print(f'{s}{h}{s}')
