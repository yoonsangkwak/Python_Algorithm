# 14490번

from math import gcd

n, m = map(int, input().split(":"))

common = gcd(n, m)
answer_1 = n // common
answer_2 = m // common
print(f"{answer_1}:{answer_2}")