# 숫자가 들어있는 리스트가 주어졌을 때, 리스트의 합을 리턴하는 함수를 만드세요. (재귀함수 활용)
import random

data = random.sample(range(100), 10)


def sum_list(data):
    if len(data) <= 1:
        return data[0]
    return data[0] + sum_list(data[1:])


print(data)
print(sum_list(data))
