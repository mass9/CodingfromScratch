for x in range(1,int(input()) + 1):
    b = [] # array
    p = list(map(int,input().split())) # [9,6]

    if x >=1 and x%2 ==0:
        p.reverse()
    
    for st in range(int(input())):
        flag = list(map(int(),input().split())) # [1,1]
        b.append(p[0]*flag[0])
        b.append(p[1]*flag[1])

    print(sum(b))
