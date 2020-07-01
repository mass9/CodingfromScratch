t = int(input()) #testcase
for _ in range(t):
    n = int(input()) #number of elements
    es = [int(x) for x in input().split()]
    xor = 0
    first = 0
    for i in range(n):
        xor ^= es[i]
        print('xor:',xor)
    
    print('final xor:',xor)
    
    result = xor
    for i in range(n):
        first ^= es[i]
        print('first:',first)
        second = xor^first
        print('second:',second)


        if (first and second) >= result:
            result = (first and second)
            print('result:',result)
    print(result)
