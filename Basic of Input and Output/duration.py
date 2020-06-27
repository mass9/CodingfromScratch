t = int(input())
for _ in range(t):
    sh,sm,eh,em = list(map(int,input().split()))
    if em < sm:
        em +=60
        eh -=1
    
    e = em-sm
    s = eh-sh
    print(s , ' ',e)