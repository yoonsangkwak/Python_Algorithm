# 11728번
# https://yoonsang-it.tistory.com/

import sys

n, m = map(int, sys.stdin.readline().split())
n_list = list(map(int, sys.stdin.readline().split()))
m_list = list(map(int, sys.stdin.readline().split()))
answer_list = n_list + m_list
answer = ' '.join(map(str, sorted(answer_list)))
print(answer)