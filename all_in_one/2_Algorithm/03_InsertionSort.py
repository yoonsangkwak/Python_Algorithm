"""
# 삽입 정렬 (Insertion Sort)
1. 삽입 정렬 (insertion sort)이란?
- 삽입 정렬은 두 번째 인덱스부터 시작
- 해당 인덱스 (key 값) 앞에 있는 데이터 (B)부터 비교해서 key값이 더 작으면, B값을 뒤 인덱스로 복사
- 이를 key 값이 더 큰 데이터를 만날때 까지 반복, 그리고 큰 데이터를 만난 위치 바로 뒤에 key 값을 이동

3. 알고리즘 구현
1) for stand in range(len(data_list)) 로 반복
2) key = data_list[stand]
3) for num in range(stand, 0, -1) 반복
    - 내부 반복문 안에서 data_list[stand] < data_list[num - 1]이면,
    - data_list[num - 1], data_list[num] = data_list[num], data_list[num - 1]

4. 알고리즘 분석
- 반복문이 두 개 O(𝑛2)
- 최악의 경우, 𝑛∗(𝑛−1) / 2
- 완전 정렬이 되어있는 상태라면 최선은 O(n)
"""

import random


def insertion_sort(data):
    for index in range(len(data) - 1):
        for index2 in range(index + 1, 0, -1):
            if data[index2] < data[index2 - 1]:
                data[index2], data[index2 - 1] = data[index2 - 1], data[index2]
            else:
                break
    return data


data_list = random.sample(range(100), 10)
print(data_list)
print(insertion_sort(data_list))
