# 10867번

n = int(input())
num_list = list(map(int, input().split()))
set_list = set(num_list)
sorted_list = sorted(set_list)
answer = " ".join([str(i) for i in sorted_list])
print(answer)