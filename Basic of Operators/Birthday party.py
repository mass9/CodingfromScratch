t = int(input())
for i in range(t):
    n,m = [int(x) for x in input().split()]
    if m%n == 0:
        print('Yes')
    else:
        print('No')
