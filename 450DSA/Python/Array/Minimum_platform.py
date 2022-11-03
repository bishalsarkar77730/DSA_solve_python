# Arrival = arr
# Departure = dep
# Time Format = HHMM (For Example = 0900 is equal to HH = 09, MM = 00 )
# Question :- Minimum Platforms Link :- https://practice.geeksforgeeks.org/problems/minimum-platforms-1587115620/1

arr = '0900, 1100, 1235'
dep = '1000, 1200, 1240'
Arrival = arr.split(',')
Departure = dep.split(',')
n = len(Arrival)
Trains = []
for i in range(n):
    Trains.append([Arrival[i], 'a'])
    Trains.append([Departure[i], 'd'])
# sorting order first according to time and if time is same for two events then arrival
# comes first followed by departure
Trains.sort(key=lambda x: x[1])
Trains.sort()
result = 1
Needed_platforms = 0
for i in Trains:
    # if the second value of vector element is 'a' which stands
    # for arrival then we add 1 to platform needed else we
    # subtract 1 from platform needed.
    if i[1] == 'a':
        Needed_platforms += 1
    else:
        Needed_platforms -= 1
    result = max(result, Needed_platforms)
print(result)
