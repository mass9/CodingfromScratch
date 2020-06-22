s = input()

xcoordinate = 0
ycoordinate = 0

for x in s:
    if x == 'L':
        xcoordinate -= 1
    elif x == 'R':
        xcoordinate += 1
    elif x == 'D':
        ycoordinate -=1
    elif x == 'U':
        ycoordinate +=1
    else:
        continue

print(xcoordinate,ycoordinate)