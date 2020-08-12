b = []
for _ in range(5):
    r = [int(x) for x in input().split()]
    b.append(r)

# print(b) # simple array
for i in range(5):
    for j in range(5):
        if b[i][j] == 1:
            r,c = i,j
# print('row: ',r)
# print('col: ',c)
# print('Step to make beautiful matrix is: ',( abs(2-r) + abs(2-c)))
print(( abs(2-r) + abs(2-c)))