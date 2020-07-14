"""
S = Distance  between A and B in km
X = km atmost in one day
N = exception days
T = on a given day
Y = travel distance on the given day
"""

s,x,n = [int(x) for x in input().split()]
count , ti, yi = 0,0,0 
b = []
for _ in range(n):
    t = [int(i) for i in input().split()]
    b.append(t)
b.sort()
while s > 0:
    # t , y = [int(x) for x in input().split()]
    s = s - x
    count +=1
    ti +=1
    yi +=1
    print('yi: ',yi)
    print('ti: ',ti)
    bl = len(b)

    if ti == b[0][0]:
        print('Exception of the day')
        
print(count)
print(b)