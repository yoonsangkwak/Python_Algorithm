# 2523번

n = int(input())

for i in range(1, 2 * n):
    if i < (2*n) // 2:
        star = "*" * i
        print(star)
    else:
        star = "*" * (2*n - i)
        print(star)