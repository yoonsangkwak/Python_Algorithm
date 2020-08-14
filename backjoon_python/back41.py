# 7568번

case = int(input())
dungch = []

for i in range(case):
    weight, height = map(int, input().split())
    dungch.append((weight, height))
    

for i in dungch:    # i는 현재 사람
    rank = 1    # 나보다 덩치 큰 사람 수 + 1
    for j in dungch:    # j는 다음 사람
        if i[0] != j[0] and i[1] != j[1]:   # 자신을 제외하고 비교
            if i[0] < j[0] and i[1] < j[1]: # [0]는 몸무게, [1]는 키
                rank += 1

    print(rank)