# 2439번

case = int(input())
star = ""

for i in range(case):
    star = " " * (case - (i+1)) + "*" * (i+1)
    print(star)