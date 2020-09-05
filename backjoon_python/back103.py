# 10870번
# https://yoonsang-it.tistory.com/

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    return fibonacci(n - 2) + fibonacci(n - 1)

n = int(input())
print(fibonacci(n))