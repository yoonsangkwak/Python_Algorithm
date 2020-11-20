# 11721번

words = input()
words_length = len(words) // 10

for _ in range(words_length + 1):
    print(words[:10])
    words = words[10:]