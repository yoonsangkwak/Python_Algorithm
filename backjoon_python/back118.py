# 11651번
# https://yoonsang-it.tistory.com/

import sys

n = int(sys.stdin.readline())

location_list = []
for _ in range(n):
    location = tuple(map(int, sys.stdin.readline().split()))
    location_list.append(location)

sorted_list = sorted(location_list, key=lambda x : (x[1], x[0]))
for i in range(len(sorted_list)):
    answer = " ".join([str(j) for j in sorted_list[i]])
    print(answer)