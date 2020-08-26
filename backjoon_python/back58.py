# 2872번

book = int(input())
book_list = []

for i in range(book):
    book_list.append(int(input()))

count = len(book_list) - 1
max_num = len(book_list)
max_num_idx = book_list.index(max_num)

for j in range(len(book_list)):
    if max_num - 1 in book_list[:max_num_idx]:
        count -= 1
        max_num -= 1
        max_num_idx = book_list.index(max_num)

print(count)
