# 1929번
# https://yoonsang-it.tistory.com/

m, n = map(int, input().split())

prime_list = [True] * (n + 1)
x = int((n + 1) ** 0.5)

for i in range(2, x + 1):
    if prime_list[i] == True:
        for j in range(i + i, n + 1, i):
            prime_list[j] = False

sieve = [i for i in range(2, n + 1) if prime_list[i] == True]

for i in range(len(sieve)):
    if sieve[i] >= m:
        print(sieve[i])