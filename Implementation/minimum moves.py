t = int(input())

while t > 0:
    count = 0
    x,y = 0,0
    x1,y1 = [int(x) for x in input().split()]
    if x<x1 and y < y1 :
        x+=1
        y+=1
        count +=1
    elif  x<x1 and y == y1:
        x+=1 
        count +=1
    
    ans =  count if count>0 else -1
    print(ans)