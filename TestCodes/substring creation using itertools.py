from itertools import combinations

# intializing string
#test_str = 'Greeks' len=21
test_str = 'baceb'

print('Original string is: '+str(test_str))

# Get all the substrings of string
res = [test_str[x:y] for x,y in combinations(
    range(len(test_str) +1),2)]

print('All substrings are: ',res)
print('Length:',len(res))