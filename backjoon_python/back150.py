# 10828번
# https://yoonsang-it.tistory.com/

from collections import deque
import sys

def func(a, b):
    if a == "push":
        stack.append(b)

def func2(c):
    if c == "size":
        return len(stack)
    elif c == "pop":
        if len(stack) != 0:
            return stack.pop()
        else:
            return -1
    elif c == "empty":
        if len(stack) == 0:
            return 1
        else:
            return 0
    elif c == "top":
        if len(stack) == 0:
            return -1
        else:
            return stack[-1]


stack = deque()

n = int(sys.stdin.readline())

for _ in range(n):
    command = sys.stdin.readline().strip().split(" ")
    if len(command) == 1:
        a = command[0]
        print(func2(a))
    else:
        a = command[0]
        b = int(command[1])
        func(a, b)