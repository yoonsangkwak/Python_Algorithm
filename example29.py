# split
my_string = "1. 2. 3. 4. 5. 6"
print(my_string.split(". "))

full_name = "Kim, Yuna"
print(full_name.split(", "))

name_data = full_name.split(", ")
last_name = name_data[0]
first_name = name_data[1]

print(first_name, last_name)
print()

print("    \n\n   2   \t    3   \n   5 7 11   \n\n".split())

numbers = "    \n\n   2   \t    3   \n   5 7 11   \n\n".split()
print(numbers[0] + numbers[1])
print(int(numbers[0]) + int(numbers[1]))