# 1712번

a, b, c = map(int, input().split())

produce = 0

if b >= c:
    produce = -1
else:
    produce = a // (c - b) + 1

print(produce)