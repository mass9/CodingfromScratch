s = input()
s = s.replace('+','')
s = [int(x) for x in s]
s.sort()
s1 = ''.join(str(e) for e in s)
print('+'.join(s1))