# 1003번
# https://yoonsang-it.tistory.com/

import sys

zero_cache = dict()
def fibonacci_zero(n):
    if n in zero_cache:
        return zero_cache[n]

    if n == 0:
        zero_cache[0] = 1
        return 1
    elif n == 1:
        zero_cache[1] = 0
        return 0
    
    result = fibonacci_zero(n-2) + fibonacci_zero(n-1)
    zero_cache[n] = result
    return result
    

one_cache = dict()
def fibonacci_one(n):
    if n in one_cache:
        return one_cache[n]

    if n == 0:
        one_cache[0] = 0
        return 0
    elif n == 1:
        one_cache[1] = 1
        return 1
    
    result = fibonacci_one(n-2) + fibonacci_one(n-1)
    one_cache[n] = result
    return result


T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    print(f"{fibonacci_zero(n)} {fibonacci_one(n)}")