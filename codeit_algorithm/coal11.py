'''
def trapping_rain(buildings):
    # 코드를 작성하세요
    rain = 0
    high = 0
    highest = max(buildings)

    for i in range(len(buildings)):
        
        if buildings[i] >= high and buildings[i] != highest:
            high = buildings[i]
        elif buildings[i] < high:
            rain += high - buildings[i] 
        elif buildings[i] == highest and i != len(buildings)-1:
            other_highest = max(buildings[i+1:])
            for j in range(i+1, len(buildings)-1):
                rain += other_highest - buildings[j]
            return rain
    
    return rain
'''
def trapping_rain(buildings):
    # 총 담기는 빗물의 양을 변수에 저장
    total_rain = 0

    # 리스트의 각 인덱스을 돌면서 해당 칸에 담기는 빗물의 양을 구한다
    # 0번 인덱스와 마지막 인덱스는 볼 필요 없다 (어차피 빗물이 안담기니까)
    for i in range(1, len(buildings) - 1):
        # 현재 인덱스를 기준으로 양쪽에 가장 높은 건물의 위치를 구한다
        max_left = max(buildings[:i])
        max_right = max(buildings[i:])

        # 현재 인덱스에 빗물이 담길 수 있는 높이
        can_rain = min(max_left, max_right)

        # 현재 인덱스에 담기는 빗물의 양을 계산
        # 만약 can_rain이 현재 인덱스 건물보다 높지 않다면, 현재 인덱스에 담기는 빗물은 0
        total_rain += max(0, can_rain - buildings[i])

    return total_rain


# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))