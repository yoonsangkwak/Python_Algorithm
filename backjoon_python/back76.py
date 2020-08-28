# 2775번

T = int(input())

def home(k, n):
    if k == 0:
        return n
    people = 0
    for j in range(1, n+1):
        people += home(k-1, j)
    return people


for i in range(T):
    k = int(input())
    n = int(input())
    print(home(k, n))