# 1026번
# https://yoonsang-it.tistory.com/

n = int(input())

a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

s = 0
for i in range(n):
    s += min(a_list) * max(b_list)
    a_list.pop(a_list.index(min(a_list)))
    b_list.pop(b_list.index(max(b_list)))

print(s)



'''
sorted_a = sorted(a_list, reverse=True)
sorted_b = sorted(b_list)

s = 0
for i in range(n):
    s += sorted_a[i] * sorted_b[i]

print(s)
'''