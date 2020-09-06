# 10814번
# https://yoonsang-it.tistory.com/

n = int(input())
user_list = []

for i in range(n):
    user = input().split()
    user.append(i)
    user_list.append(user)

sorted_list = sorted(user_list, key=lambda x : (int(x[0]), x[2]))
for i in range(len(sorted_list)):
    answer = " ".join(sorted_list[i][:2])
    print(answer)