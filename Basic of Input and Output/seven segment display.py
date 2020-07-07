t = int(input()) #testcases
segement = [6,2,5,5,4,5,6,3,7,6]
for _ in range(t):
    s = input()
    print('s:',s)
    total = 0
    for  x in s:
        x = int(x)
        total +=segement[x]
    one = total//2
    if total%2 == 0:
        ans = '1'*one
    else:
        ans = '7' + '1'*(one-1)
    print(ans)