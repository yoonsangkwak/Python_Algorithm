# 10808번

from string import ascii_lowercase

alpha_list = list(ascii_lowercase)
count_list = [0] * 26

word = input()

for alpha in word:
    i = alpha_list.index(alpha)
    count_list[i] += 1

print(" ".join(map(str, count_list)))