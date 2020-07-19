# 1789번

'''
number_sum = int(input(""))


def func(num):
    i = 1
    integer_sum = 0
    while i <= num:
        integer_sum = integer_sum + i
        i += 1
    return integer_sum


j = 1
while j < number_sum:
    if func(j) > number_sum:
        print(j - 1)
        break
    else:
        j += 1
'''

s = int(input())
n = 1
while n * (n + 1) / 2 <= s:
    n += 1
print(n - 1)