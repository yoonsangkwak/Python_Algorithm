"""
def multiple(num):
    return_value = 1
    for index in range(1, num + 1):
        return_value = return_value * index
    return return_value
"""


# 재귀 함수를 활용해서 1부터 num까지의 곱이 출력되게 만드세요
def multiple(num):
    if num <= 1:
        return num
    return num * multiple(num - 1)


print(multiple(5))
