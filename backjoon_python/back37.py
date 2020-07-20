# 10214번

T = int(input())

for num in range(T):
    yonsei = 0
    korea = 0
    for i in range(9):
        hoi = input().split()
        yonsei += int(hoi[0])
        korea += int(hoi[1])
    if yonsei > korea:
        print("Yonsei")
    elif yonsei < korea:
        print("Korea")
    elif yonsei == korea:
        print("Draw")
