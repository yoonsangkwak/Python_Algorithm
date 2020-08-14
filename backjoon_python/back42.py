# 3047번

a, b, c = map(int, input().split())
temp = input()

x = [a, b, c]
x.sort()
for i in range(len(x)):
    if temp[i] == "A":
        print(x[0])
    elif temp[i] == "B":
        print(x[1])
    elif temp[i] == "C":
        print(x[2])