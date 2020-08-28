# 2908번

a, b = input().split()

reverse_a = a[::-1]
reverse_b = b[::-1]

if int(reverse_a) > int(reverse_b):
    print(reverse_a)
else:
    print(reverse_b)