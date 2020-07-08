s,i = input().split()
s= list(s)
i = int(i)
n = ''
for x in range(len(s)):
    if s[x] != '9' and i > 0:
        n += '9'
        i -=1
    else:
        n += s[x]

print(n)