# 2490번

for _ in range(3):
    yut = input().split()
    zero = 0
    one = 0
    
    for i in yut:
        if i == "0":
            zero += 1
        elif i == "1":
            one += 1
    
    if one == 1:
        print("C")
    elif one == 2:
        print("B")
    elif one == 3:
        print("A")
    elif one == 4:
        print("E")
    elif one == 0:
        print("D")