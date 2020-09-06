# 2751번
#https://yoonsang-it.tistory.com/

import sys

n = int(sys.stdin.readline())

num_list = []
for _ in range(n):
    num_list.append(int(sys.stdin.readline()))

sorted_list = sorted(num_list)
for number in sorted_list:
    print(number)