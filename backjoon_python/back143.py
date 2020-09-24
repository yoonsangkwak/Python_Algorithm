# 10995번

n = int(input())

if n == 1:
    print("*")
else:
    for i in range(1, n + 1):
        if i % 2 == 1:
            print(("*" + " ") * n)
        else:
            print((" " + "*") * n) 