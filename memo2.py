import os
os.system('cls')

# [표현식 for 항목 in 리스트 or 튜플 if 조건문]

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 리스트 안에서 for문 사용하기 1
# 리스트 각 항목에 3을 곱한 결과를 다시 원래 리스트에 대입
list = [i * 3 for i in list]
print(list)
print()

# 리스트 안에서 for문 사용하기 2 : if문 사용
# 리스트 각 항목 중 홀수만 따로 뽑아서 3을 곱한 결과를 다시 대입
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list = [num * 3 for num in list if num % 2 == 1]
print(list)
print()

# 리스트 안에서 for문 사용하기 3 : 두 개 이상의 for문
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list = [num * num2 for num in list if num % 2 == 1
for num2 in list if num2 % 2 == 1]
print(list)
print()

# 리스트 안에서 for문 사용하기 4 : range() 메서드 활용
# 구구단
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list = [x * y for x in range(1, 10)
for y in range(1, 10)]
print(list)