n , k = [int(x) for x in input().split()]
e = [int(i) for i in input().split()]

b = []
ei = e[k-1]
# print('ei:',ei)
for i in e:
    if i >= ei and i > 0:
        b.append(i)

print(len(b))