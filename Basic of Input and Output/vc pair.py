vowels = {'a','e','i','o','u'} 
def number_world(number): # number of string
    s = input() # input of the string
    count = 0
    #print('They are equal')
    for i in range(n):
        if i!=n-1:
            if s[i] not in vowels and s[i+1] in vowels:
                count +=1
    print(count)

t = int(input()) # number of testcases
while t >0:
    n = int(input()) # number for the length of the string
    number_world(n)
    t -= 1

