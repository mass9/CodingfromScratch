from sys import stdin,stdout
import math
t=stdin.readline()
t=int(t)
for _ in range(t):
    l,r,s=[int(x) for x in stdin.readline().split()]
    if(s>r or math.ceil(l/s)>math.floor(r/s)):
        print("-1 -1")
    else:
        print(math.ceil(l/s),math.floor(r/s))