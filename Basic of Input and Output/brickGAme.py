n = int(input())

for i in range(n):
    n = n-i 
    if n < 0:
        print('Patlu')
        break
    
    n= n -i*2 
    if n< 0:
        print('Motu')
        break