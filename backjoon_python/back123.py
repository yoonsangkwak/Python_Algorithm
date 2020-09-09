# 2108번
# https://yoonsang-it.tistory.com/

from collections import Counter
import sys

def Arithmetic_mean(some_list):
    list_sum = 0
    for i in some_list:
        list_sum += i

    return round(list_sum / len(some_list))


def median(some_list):
    sorted_list = sorted(some_list)
    center = len(sorted_list) // 2

    return sorted_list[center]


def mode(some_list):
    count = Counter(some_list)
    count_order = count.most_common()
    maximum = count_order[0][1]

    modes = []
    for i in count_order:
        if i[1] == maximum:
            modes.append(i[0])

    sorted_modes = sorted(modes)
    if len(sorted_modes) > 1:
        return sorted_modes[1]
    else:
        return sorted_modes[0]


def difference(some_list): 
    sorted_list = sorted(some_list)
    diff = sorted_list[-1] - sorted_list[0]
    return diff


n = int(sys.stdin.readline())
num_list = []

for _ in range(n):
    num_list.append(int(sys.stdin.readline()))

print(Arithmetic_mean(num_list))
print(median(num_list))
print(mode(num_list))
print(difference(num_list))