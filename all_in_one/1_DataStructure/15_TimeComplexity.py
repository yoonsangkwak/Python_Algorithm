"""
# 알고리즘 복잡도 표현 방법

1. 알고리즘 복잡도 계산이 필요한 이유
- 하나의 문제를 푸는 알고리즘은 다양할 수 있음
    ex) 정수의 절대값 구하기
    - 방법1 : 정수값을 제곱한 값에 다시 루트를 씌우기
    - 방법2 : 정수가 음수인지 확인해서, 음수일 때만 -1을 곱하기

2. 알고리즘 복잡도 계산 항목
    1) 시간 복잡도 : 알고리즘 실행 속도
    2) 공간 복잡도 : 알고리즘이 사용하는 메모리 사이즈

- 시간 복잡도의 주요 요인 : 반복문

알고리즘 성능 표기법
- Big O (빅-오) 표기법 : O(N)
    - 알고리즘 최악의 실행 시간을 표기
    - 가장 많이 / 일반적으로 사용함
    - 아무리 최악의 상황이라도, 이정도의 성능은 보장한다는 의미이기 때문
- 오메가 표기법 : Ω(N)
    - 알고리즘 최상의 실행 시간을 표기
- 세타 표기법 : θ(N)
    - 알고리즘 평균 실행 시간을 표기

3. 대문자 O 표기법
- 빅 오 표기법, Big-O 표기법 이라고도 부름
- O(입력)
    - 입력 n에 따라 결정되는 시간 복잡도 함수
    - O(1), O(n), O(logN) 등으로 표기함
    - 입력 n의 크기에 따라 기하급수적으로 시간 복잡도가 늘어날 수 있음
    - O(1) < O( 𝑙𝑜𝑔𝑛 ) < O(n) < O(n 𝑙𝑜𝑔𝑛 ) < O( 𝑛2 ) < O( 2𝑛 ) < O(n!)
    - 참고: log n 의 베이스는 2 -  𝑙𝑜𝑔2𝑛
- 표현식에 가장 큰 영향을 미치는 n의 단위로 표기
"""

# 1부터 n까지의 합을 구하는 알고리즘1
# - 입력 n에 따라 덧셈을 n번 해야함 (반복문)
# - 시간 복잡도 : n, 빅 오 표기법으로는 O(n)
def sum_all(n):
    total = 0
    for num in range(1, n + 1):
        total += num
    return total

print(sum_all(100))


# 1부터 n까지의 합을 구하는 알고리즘2
# - 입력 n이 어떻든 간에, 곱셈/덧셈/나눗셈 하면 됨 (반복문 없음)
# - 시간 복잡도 : 1, 빅 오 표기법으로는 O(1)
def sum_all2(n):
    return n * (n+1) / 2

print(sum_all2(100))