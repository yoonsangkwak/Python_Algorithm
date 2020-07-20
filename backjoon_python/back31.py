# 5717번

while True:
    boy, girl = map(int, input().split())
    if boy == girl == 0:
        break
    print(boy + girl)