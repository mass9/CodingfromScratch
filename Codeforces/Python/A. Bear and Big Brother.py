l,b = [int(x) for x in input().split()]
year_count =0

while (b>=l):
    l=l*3
    b=b*2
    # print('bob:',b)
    # print('limik:',l)
    year_count+=1

print(year_count)