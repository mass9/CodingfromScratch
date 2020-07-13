n , qs = [x for x in input().split()]
n_elements = [ int(i) for i in input().split()]

for _ in range(int(qs)):
    q = [int(j) for j in input().split()]
    if q[0] == 1:
        n_elements[q[1]] = q[2]
        # print('n_elements:',n_elements)

    else:
        l , r = q[1] , q[2]
        # print('l:',l)
        # print('r:',r)
        # print('n_elements:',n_elements)
        print(sum(n_elements[l:r+1]))