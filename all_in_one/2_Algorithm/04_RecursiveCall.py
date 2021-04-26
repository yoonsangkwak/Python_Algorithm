"""
재귀 용법 (recursive call, 재귀 호출)
- 함수 안에서 동일한 함수를 호출하는 형태

예제 1번)
- factorial(n)은 n - 1번의 factorial() 함수를 호출해서, 곱셈을 함
    - 일종의 n - 1번 반복문을 호출한 것과 동일
    - factorial() 함수를 호출할 때마다, 지역변수 n이 생성됨
- 시간 복잡도 / 공간 복잡도는 둘 다 O(n)

재귀 호출의 일반적인 형태
1) 일반적인 형태 1
def function(입력):
    if 입력 > 일정값:    # 입력이 일정 값 이상이면
        return function(입력 - 1)     # 입력보다 작은 값
    else:
        return 일정값, 입력값, 또는 특정값     # 재귀 호출 종료

2) 일반적인 형태 2
def function(입력):
    if 입력 <= 일정값:   # 입력이 일정 값보다 작으면
        return 일정값, 입력값, 또는 특정값     # 재귀 호출 종료
    function(입력보다 작은 값)
    return 결과값

재귀 호출은 스택의 전형적인 예
- 함수는 내부적으로 스택처럼 관리된다
- 참고 : 파이썬에서는 재귀 함수 깊이가 1000회 이하가 되어야 한다
"""


# 일반적인 형태 1
def factorial(num):
    if num > 1:
        return num * factorial(num - 1)
    else:
        return num


for num in range(5):
    print(factorial(num))

print()


# 일반적인 형태 2
def factorial2(num):
    if num <= 1:
        return num
    return num * factorial2(num - 1)


for num in range(5):
    print(factorial2(num))
