vowels = {'a','e','i','o','u'}
count = 1 
def number_world(number): # number of string
    s = input() # input of the string
    if len(s) == n:
        print('They are equal')
        for i in s:
            if i in vowels and s.index(i) > 0:

                print('Yeah, this vowels:',i)
    else:
        print('They are not equal')

t = int(input()) # number of testcases
while t >0:
    n = int(input()) # number for the length of the string
    number_world(n)
    t -= 1

