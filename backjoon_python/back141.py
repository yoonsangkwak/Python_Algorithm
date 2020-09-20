# 17828번
# https://yoonsang-it.tistory.com/

import sys

n, x = map(int, sys.stdin.readline().split())

alpha_key = []
alpha_value = []

for i in range(26):
    alpha_key.append(chr(90 - i))
    alpha_value.append(26 - i)

answer_list = []

if (26 * n) < x or n > x:
    answer_list.append("!")
else:
    for i in range(len(alpha_value)):
        if x // alpha_value[i] > 0 and x % alpha_value[i] >= n - (len(answer_list) + x // alpha_value[i]):
            for j in range(x // alpha_value[i]):
                answer_list.append(alpha_key[i])
            x %= alpha_value[i]
    
    answer_list.sort()

answer = "".join(map(str, answer_list))

print(answer)