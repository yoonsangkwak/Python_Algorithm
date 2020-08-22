def staircase(n):
    if n < 2:
        return 1
    
    stair_one = 1
    stair_two = 1
    current = stair_one + stair_two
    for i in range(2, n):
        stair_two = stair_one
        stair_one = current
        current = stair_one + stair_two
    
    return current

'''
def staircase(n):
    a, b = 1, 1
    for i in range(n):
        a, b = b, a + b
    return a
'''


# 테스트
print(staircase(0))
print(staircase(6))
print(staircase(15))
print(staircase(25))
print(staircase(41))
