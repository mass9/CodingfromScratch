t = int(input())
while t >0:
    s = input()
    if len(s) > 10:
        l=len(s[1:-1])
        print(s[0] + str(l) + s[-1])
    else:
        print(s)
    t -=1