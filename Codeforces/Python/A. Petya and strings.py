s1 = input()
s2 = input()
s1,s2 = s1.lower(),s2.lower()
result = 0
# if s1 is less then print -1
# if s2 is less print 1
# if both are same print  0
if s1 < s2:
    result = -1
if s1 >s2:
    result = 1
print(result)
