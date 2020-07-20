# 5086번

'''
while True:
    case = input().split()
    test = []
    test.append(int(case[0]))
    test.append(int(case[1]))

    if test[0] < test[1]:
        if test[1] % test[0] == 0:
            print("factor")
        else:
            print("neither")
    elif  test[0] > test[1]:
        if test[0] % test[1] == 0:
            print("multiple")
        else:
            print("neither")
    elif test[0] == test[1] == 0:
        break
'''

while True:
    A, B = map(int, input().split())
    if A == B == 0:
        break
    elif A % B == 0:
        print("multiple")
    elif B % A == 0:
        print("factor")
    else:
        print("neither")