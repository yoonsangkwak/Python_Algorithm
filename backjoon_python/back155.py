# 2747번

n = int(input())

fib_a = 0
fib_b = 1

for i in range(n):
    fib = fib_a + fib_b
    fib_a, fib_b = fib, fib_a

print(fib)