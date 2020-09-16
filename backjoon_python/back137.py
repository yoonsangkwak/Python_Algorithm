# 9093번
# https://yoonsang-it.tistory.com/

T = int(input())

for _ in range(T):
    text = input().split()
    answer_list = []

    for word in text:
        answer_list.append(word[::-1])

    answer = " ".join(answer_list)
    print(answer)