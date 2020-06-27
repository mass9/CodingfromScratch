n=input()
total =0
number = 1
if len(n) == 10:    
    for i in n:
        n1 = int(i)
        total += n1 * number
        number += 1
    if total % 11 == 0:
        print('Legal ISBN')
    else:
        print('Illegal ISBN')
else:
    print('Illegal ISBN')