n , qs = [x for x in input().split()]
n_elements = [ int(i) for i in input().split()]

for _ in range(int(qs)):
    q = [j for j in input().split()]
    if q[0] == '1':
        qs[q[2]] = '5'
    print(qs)