
# Write your code here
d = int(input()) # Distance from home to offide
oc,of, od = [int(x) for x in input().split()]
cs,cb,cm,cd = [int(x) for x in input().split()]

Cost_Online = oc + (d - of)*od
Cost_Offline = cb+(d/cs)*cm+ (d*cd)

if Cost_Online == Cost_Offline:
    print('Online Taxi')
elif Cost_Offline < Cost_Online:
    print('Classic Taxi')
else:
    print('Online Taxi')