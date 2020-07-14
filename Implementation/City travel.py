import math

def city(a,b,l):
    p = 0
    q = 0
    day = 1
    while(p<a):
        if q<len(l) and day!=l[q][0]: # if exception day is not in sequece
            if int(math.ceil((a-p)/b)) > l[q][0] -day:  
                s = l[q][0] - day
                print('s1:',s)
                p = p + b*s
                print('p1:',p)
                if p >=a:
                    return day
                else:
                    day = l[q][0]
                    print('day2:',day)
            else:
                day = day + (int(math.ceil((a-p)/b)) -1)
                p = a
            
        elif q<len(l) and day == l[q][0]: # excecption day
            p = p + l[q][1]
            if p >= a:
                return day
            else:
                day +=1
                q +=1
        
        else:
            s = a-p
            day = day + int(math.ceil((a-p)/b)) -1
            p = a
        
    return day
n = list(map(int,input().split()))
l = []
for i in range(n[2]):
    a = list(map(int,input().split()))
    l = l+[[a[0],a[1]]]
    l.sort()

print(city(n[0],n[1],l))