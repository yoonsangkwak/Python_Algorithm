# 12871번
# https://yoonsang-it.tistory.com/

from math import gcd

def lcm(x, y):
    return x * y // gcd(x, y)


s = input()
t = input()

n = lcm(len(s), len(t))

if s * (n // len(s)) == t * (n // len(t)):
    answer = 1
else:
    answer = 0

print(answer)