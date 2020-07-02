n =  int(input()) # size of an array
x = [x for x in input().split()]
b=[]
sep = n//2
first_half,second_half = x[:sep],x[sep:]

for i in first_half:
    s = i[0]
    b.append(s)

for j in second_half:
    s = j[-1]
    b.append(s)
number = ''.join(b)
if (int(number)) %11 ==0:
    print('Yes')
else:
    print('No')