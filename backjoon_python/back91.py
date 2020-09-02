# 10809번

s = input()
alphabet = "abcdefghijklmnopqrstuvwxyz"
answer_list = []

for i in range(len(alphabet)):
    if alphabet[i] in s:
        check = s.index(alphabet[i])
        answer_list.append(str(check))
    else:
        answer_list.append("-1")

answer = " ".join(answer_list)
print(answer)