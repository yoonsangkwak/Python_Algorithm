"""
대표적인 정렬 1 : 버블 정렬 (bubble sort)

1. 정렬 (sorting) 이란?
- 정렬 (sorting) : 어떤 데이터들이 주어졌을 때 이를 정해진 순서대로 나열하는 것
- 정렬은 프로그램 작성시 빈번하게 필요로 함
- 다양한 알고리즘이 고완되었으며, 알고리즘 학습의 필수
    - 다양한 알고리즘 이해를 통해, 동일한 문제에 대해 다양한 알고리즘이 고안할 수 있음을 이해하고,
    각 알고리즘간 성능 비교를 통해, 알고리즘 성능 분석에 대해서도 이해할 수 있음

2. 버블 정렬 (bubble sort)이란?
- 두 인접한 데이터를 비교해서, 앞에 있는 데이터가 뒤에 있는 데이터보다 크면, 자리를 바꾸는 정렬 알고리즘

4. 알고리즘 구현
- 특이점 찾아보기
    - n개의 리스트가 있는 경우 최대 n-1번의 로직을 적용한다.
    - 로직을 1번 적용할 때마다 가장 큰 숫자가 뒤에서부터 1개씩 결정된다.
    - 로직이 경우에 따라 일찍 끝날 수도 있다. 따라서 로직을 적용할 때
    한 번도 데이터가 교환된 적이 없다면 이미 정렬된 상태이므로 더 이상 로직을 반복 적용할 필요가 없다.

1) for num in range(len(data_list)) 반복
2) swap = 0 (교환이 되었는지를 확인하는 변수)
3) 반복문 안에서, for index in range(len(data_list) - num - 1) -> n - 1번 반복해야 하므로
4) 반복문안의 반복문 안에서, if data_list[index] > data_list[index + 1] 이면
5) data_list[index], data_list[index + 1] = data_list[index + 1], data_list[index]
6) swap += 1
7) 반복문 안에서, if swap == 0 이면, break

5. 알고리즘 분석
- 반복문이 두 개 O(𝑛2)
    - 최악의 경우,  𝑛∗(𝑛−1) / 2
- 완전 정렬이 되어 있는 상태라면 최선은 O(n)
"""


def bubble_sort(data):
    for i in range(len(data) - 1):
        swap = False
        for j in range(len(data) - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swap = True

        if swap == False:
            break

    return data


import random

# data_list = random.sample(range(100), 4)
data_list = [2, 3, 1, 5, 4]
print(data_list)
print(bubble_sort(data_list))