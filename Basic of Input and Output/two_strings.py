for x in range(int(input())):
    s1 ,s2 = input().split()
    s1 , s2 = sorted(s1),sorted(s2)
    if s1 == s2:
        print('YES')
    else:
        print('NO')
