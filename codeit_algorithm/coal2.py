
def binary_search(element, some_list):
    # 코드를 작성하세요.
    start = 0
    end = len(some_list) - 1
    while start <= end:
        center = (start + end) // 2
        if some_list[center] == element:
            return center
        elif element < some_list[center]:
            end = center - 1
        else:
            start = center + 1


'''
def binary_search(element, some_list):
    center = 0
    while len(some_list) != 0:
        mid = len(some_list) // 2

        if element > some_list[mid]:
            some_list = some_list[mid + 1:]
            center += mid + 1
        elif element < some_list[mid]:
            some_list = some_list[:mid]
        elif element == some_list[mid]:
            center += mid
            return center
    
    return None
'''


print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))