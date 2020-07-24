# Basic approach, calculate sum of all subarray and print the maximum

x = [int(x) for x in input().split()]
ans = sum(x)
b = []
for i in range(len(x)):
    for j in range(len(x)):
        s = sum(x[i:j])
        print(s)
        b.append(s)
if ans < max(b):
    ans = max(b)
print(b)
print(ans)

# Better approach

