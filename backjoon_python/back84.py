# 10871번

n, x = map(int, input().split())
num_list = list(map(int, input().split()))
answer_list = []

for i in range(len(num_list)):
    if num_list[i] < x:
        answer_list.append(num_list[i])


answer = " ".join([str(_) for _ in answer_list])

print(answer)