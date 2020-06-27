n = int(input()) #number of inputs
x = list(map(int,input().split())) # array list of the inputs
total = sum(x)
b = []

for i in range(n):
    if (total - x[i])%7==0:
        b.append(x[i])

if len(b)==0:
    print(-1)
else:
    print(x.index(min(b)))