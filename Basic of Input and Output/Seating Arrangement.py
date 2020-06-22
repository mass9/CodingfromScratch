def seatingArrangement(number):
    if number > 108:
        return -1
    divisible_Number = number%12 # find 1-12 seats
    seatformat = 'Nothing'
    if divisible_Number == 0:
        new_number = number -11
        seatformat = 'WS'
    elif divisible_Number == 1:
        new_number =  number +11
        seatformat = 'WS'
    elif divisible_Number == 6:
        new_number =  number +1
        seatformat = 'WS'
    elif divisible_Number == 7:
        new_number =  number -1
        seatformat = 'WS'
    
    elif divisible_Number == 2:
        new_number = number -9
        seatformat = 'MS'
    elif divisible_Number == 11:
        new_number =  number +9
        seatformat = 'MS'
    elif divisible_Number == 5:
        new_number =  number +3
        seatformat = 'MS'
    elif divisible_Number == 8:
        new_number =  number -3
        seatformat = 'MS'
    

    elif divisible_Number == 3:
        new_number = number +7
        seatformat = 'AS'
    elif divisible_Number == 10:
        new_number =  number -7
        seatformat = 'AS'
    elif divisible_Number == 4:
        new_number =  number  + 5
        seatformat = 'AS'
    elif divisible_Number == 9:
        new_number =  number - 5
        seatformat = 'AS'
    

    print(new_number ,' ',seatformat)
while True:
    try:
        t= int(input()) # number of testcases
        while t >0 :
            n = int(input())
            seatingArrangement(n)
            t= t-1
    except EOFError:
        break


