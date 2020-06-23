n = int(input()) #number of inputs
x = [int(x) for x in input().split()] # array list of the inputs

addition = sum(x)

for i in range(n):
    print(sum(x[i:]))