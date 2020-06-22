
def anagrams(a,b):
    count = 0
    for i in range(97,123):
        ax = sum(letter == chr(i) for letter in a)
        bx = sum(letter == chr(i) for letter in b)

        count += abs(ax-bx)
    
    return count


for i in range(int(input())):
    a = input()
    b = input()

    print(anagrams(a,b))
