# 5063번

case = int(input())

for num in range(case):
    r, e, c = map(int, input("").split())
    if r + c < e:
        print("advertise")
    elif r + c == e:
        print("does not matter")
    elif r + c > e:
        print("do not advertise")
