# 리스트 (list)
numbers = [2, 3, 5, 7, 11, 13]
names = ["윤수", "혜린", "태호", "영훈"]

# 인덱싱 (indexing)
print(names[0])
print(numbers[1] + numbers[3])
num_1 = numbers[1]
num_3 = numbers[3]
print(num_1 + num_3)
print(numbers[-1])
print(numbers[-6])

# 리스트 슬라이싱 (list slicing)
print(numbers[:3])
new_list = numbers[:3]  # [2, 3, 5]
print(new_list)
print()
numbers[0] = 7
print(numbers)
print()
numbers[0] = numbers[0] + numbers[1]
print(numbers)