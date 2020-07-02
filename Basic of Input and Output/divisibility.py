n =  int(input()) # size of an array
x = [x for x in input().split()]
b=[]
for i in x:
    b.append(i[-1])
number = ''.join(b)
if (int(number)) %10 ==0:
    print('Yes')
else:
    print('No')