# 9012번
# https://yoonsang-it.tistory.com/

from collections import deque

def parentheses_checker(string):
    stack = deque() 
    check = True

    for i in range(len(string)):
        if string[i] == "(":
            stack.append(i)
        
        if string[i] == ")":
            if stack:
                stack.pop()
            else:
                check = False
    
    if check == False or stack:
        print("NO")
    else:
        print("YES")


T = int(input())

for _ in range(T):
    string = input()
    parentheses_checker(string)