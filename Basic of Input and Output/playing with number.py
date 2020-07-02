n , q = [int(x) for x in input().split()]
b = []
totalism =0
n_elements = [int(x) for x in input().split()]

#Prefix sum matter
for x in n_elements:
    totalism += x
    b.append(totalism)
print('Prefix Sum:',b)

for i in range(q):
    l,r = [int(j) for j in input().split()]
    if l ==1:
        print(b[r -1]//r)
    else:
        print(((b[r-1]) - b[l -2]) // ((r - l) +1 ))