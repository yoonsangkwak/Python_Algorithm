import sys

n = int(sys.stdin.readline())

for _ in range(n):
    a, b = map(int, input().split())
    answer = [(a ** i) % 10 for i in range(1, 5)][(b % 4) - 1]
    print(answer if answer != 0 else 10)