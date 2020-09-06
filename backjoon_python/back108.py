# 1181번
# https://yoonsang-it.tistory.com/

n = int(input())
word_list = []

for _ in range(n): 
    a = input()
    b = len(a)
    word_list.append((a, b))

word_list = list(set(word_list))
sorted_list = sorted(word_list, key=lambda x : (x[1], x[0]))

for word in sorted_list:
    print(word[0])