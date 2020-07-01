import sys
d = int(input())
count = 0 
for _ in range(d):

    r,x = map(int,sys.stdin.readline().split())
    perimeter = 2*r*(22/7)
    h = x*100
    if perimeter < h:
        count+=1
print(count)