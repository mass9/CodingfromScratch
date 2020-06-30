from itertools import combinations

vowels='AEIOUaeiou'

# Naive approach
# def vowel_recognition(string):
    
#     count = 0
#     for x,y in combinations(range(len(string)+1),2):
#         s = string[x:y]
#         for v in s:
#             if v in vowels:
#                 count+=1
#     print(count)

def vowel_recognition(string):
    count =0 
    for i in range(len(s)):
        if s[i] in vowels:
            count += (len(s)-i)*(i+1)
    print(count)

t = int(input()) #testcases
while t >0:

    s = input()
    vowel_recognition(s)
    t -=1

