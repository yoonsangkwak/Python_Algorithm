def fib_optimized(n):
    # 코드를 작성하세요. 
    fib_current = 1
    fib_previous = 1
    if n < 3:
        return 1
    i = 3
    while i <= n:
        fib = fib_current + fib_previous
        fib_current, fib_previous = fib, fib_current
        i += 1
    return fib 



# 테스트
print(fib_optimized(16))
print(fib_optimized(53))
print(fib_optimized(213))
