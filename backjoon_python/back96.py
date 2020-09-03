# 10520번
# https://yoonsang-it.tistory.com/

case = int(input())

for _ in range(case):
    height, width, guest = map(int, input().split())

    if guest % height < 1:
        x = str(guest // height)
        y = str(height)
    else:
        x = str(guest // height + 1)
        y = str(guest % height)

    if len(x) < 2:
        x = "0" + str(x)
    
    print(y + x)