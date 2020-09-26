# 1543번
# https://yoonsang-it.tistory.com/

n = input()
m = input()

count = 0
i = 0
while i <= len(n) - len(m):
    if n[i:i + len(m)] == m:
        count += 1
        i += len(m)
    else:
        i += 1

print(count)