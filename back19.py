# 4101번

while True:
    case = input("").split()
    A = int(case[0])
    B = int(case[1])
    if A > B:
        print("Yes")
    elif A <= B and B != 0:
        print("No")
    elif A == 0 and B == 0:
        break