# 10996번

n = int(input())

for i in range(1, 2 * n + 1):
    star = ["*"] * n
    if n < 2:
        print("*")
        break

    if i % 2 == 0:
        for j in range(len(star)):
            if j % 2 == 0:
                star[j] = " "
    
    else:
        for j in range(len(star)):
            if j % 2 != 0:
                star[j] = " "

    real_star = "".join(star)
    print(real_star)