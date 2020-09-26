# 11656번
# https://yoonsang-it.tistory.com/

S = input()
answer_list = [S]

for i in range(len(S)-1):
    S = S[1:]
    answer_list.append(S)

answer = sorted(answer_list)
for i in answer:
    print(i)