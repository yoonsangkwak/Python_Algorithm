'''
numbers = []
print(len(numbers))

numbers.append(5)
numbers.append(8)
print(numbers)
print(len(numbers))
'''

numbers = [2, 3, 5, 7, 11, 13, 17, 19]
del numbers[3]
print(numbers)


numbers = [2, 3, 5, 7, 11, 13, 17, 19]
numbers.insert(4, 37)
print(numbers)