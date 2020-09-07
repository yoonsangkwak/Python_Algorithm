# 11004번
# https://yoonsang-it.tistory.com/

n, k = map(int, input().split())
n_list = list(map(int, input().split()))
sorted_list = sorted(n_list)

print(sorted_list[k-1])