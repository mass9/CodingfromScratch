t = int(input())
a = 0
b = 7
while t > 0:

    n = int(input())

    if abs(a-n) > abs(b-n):
        b = n
        print('B')
    elif abs(a-n) == abs(b-n):
        if(a<b):
            a =n
            print('A')
        else:
            b = n 
            print('B')
    elif abs(a-n) < abs(b-n):
        a = n
        print('A')
        
    else: 
        continue

    t -= 1