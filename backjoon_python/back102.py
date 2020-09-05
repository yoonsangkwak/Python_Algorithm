# 1002번
# https://yoonsang-it.tistory.com/

import math

T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    location = 0
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    if x1 == x2 and y1 == y2:
        if r1 == r2:
            location = -1
        else:
            location = 0
        continue
    
    if r1 > distance + r2 or r2 > distance + r1 or distance > r1 + r2:
        location = 0
    elif r1 == distance + r2 or r2 == distance + r1 or r1 + r2 == distance:
        location = 1
    else:
        location = 2

    print(location)