# 2231번

N = int(input())
M = 0

def get_divided_num(x):
    n = list(map(int, str(x)))
    divided_num = x + sum(n)
    return divided_num


while get_divided_num(M) != N:
    if M == N:
        M = 0
        break
    else:
        M += 1

print(M)