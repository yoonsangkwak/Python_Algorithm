# 1427번
# https://yoonsang-it.tistory.com/

n = int(input())

sorted_num = sorted(str(n), reverse=True)
string_num = "".join(sorted_num)
print(string_num)