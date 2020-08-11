t = int(input())
x = 0
while t>0:
    s = input()
    if '+' in s:
        x+=1
    if '-' in s:
        x-=1
    t-=1
print(x)
