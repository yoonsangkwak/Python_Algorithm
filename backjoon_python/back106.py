# 1037번
# https://yoonsang-it.tistory.com/

n = int(input())
num_list = list(map(int, input().split()))
sorted_list = sorted(num_list)

print(sorted_list[0] * sorted_list[-1])