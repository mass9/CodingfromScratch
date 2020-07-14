import math

sl = int(input()) # length of a string
s = input()

a = []
a.append(math.floor(s.count('h')/2))
a.append(math.floor(s.count('e')/2))
a.append(math.floor(s.count('a')/2))
a.append(math.floor(s.count('r')/2))
a.append(s.count('c'))
a.append(s.count('k'))
a.append(s.count('t'))

print(min(a))