t = int(input()) # test cases
count = 0
while t > 0:
    x = [int(x) for x in input().split()]
    if x.count(1) > 1:
        count +=1
    t -=1
print(count)