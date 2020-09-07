# 11650번
# https://yoonsang-it.tistory.com/

n = int(input())

location_list = []
for _ in range(n):
    location = tuple(map(int, input().split()))
    location_list.append(location)

sorted_list = sorted(location_list, key=lambda x : (x[0], x[1]))
for i in range(len(sorted_list)):
    answer = " ".join([str(j) for j in sorted_list[i]])
    print(answer)