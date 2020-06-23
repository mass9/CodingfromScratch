n = int(input())
s = input()
c = 0
for i in range(n-1):
    if (s[i] == s[i+1] and s[i] == 'H'):
        c += 1
if s.count('.') > 0:
    s = s.replace('.','B')

if c ==0:
    print('YES')
    print(s)
else:
    print('NO')