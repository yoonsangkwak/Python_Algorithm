# 10992번

n = int(input())

for i in range(1, n + 1):
    if i == 1:
        print(" " * (n - 1) + "*")
    elif i != n:
        print(" " * (n - i) + "*" + " " * (2 * (i - 1) - 1) + "*")
    else:
        print("*" * (2 * n - 1))