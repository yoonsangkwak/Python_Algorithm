# 5620번

n = int(input())
location_list = []

for i in range(n):
    location = tuple(map(int, input().split()))
    location_list.append(location)

def distance(location1, location2):
    return (location1[0] - location2[0]) ** 2 + (location1[1] - location2[1]) ** 2


def closest_pair(coordinates):
    pair = [coordinates[0], coordinates[1]]

    for i in range(len(coordinates) - 1):
        for j in range(i + 1, len(coordinates)):
            location1, location2 = coordinates[i], coordinates[j]

            if distance(pair[0], pair[1]) > distance(location1, location2):
                pair = [location1, location2]
    
    return pair


close = closest_pair(location_list)
print(distance(close[0], close[1]))