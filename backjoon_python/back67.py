# 2446번

case = int(input())
star = ""

for i in range((2 * case) - 1):
    if i <= ((2 * case) - 1) // 2:
        star = " " * i + "*" * (2 * (case - i) - 1)
    else:
        star = " " * ((2 * case - 1) - (i+1)) + "*" * (2 * ((i+1) - case) + 1)
    print(star)
