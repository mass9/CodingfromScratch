while True:
    try:
        n = input()
        if ('000000' in n) or ('111111' in n):
            print('Sorry, sorry!')
        else:
            print('Good luck!')
    except EOFError:
        break