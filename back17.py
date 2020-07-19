# 1934번

'''
def least(A, B):
    i = 1
    common = 1
    while i <= A or i <= B:
        if A % i == 0 and B % i == 0:
            A = A // i
            B = B // i
            common = common * i
            if i == 1:
                i += 1
        else:
            i += 1
        multi = common * (A % i) * (B % i)
    return multi

case = int(input(""))

for num in range(case):
    lcm = input("").split(" ")
    print(least(int(lcm[0]), int(lcm[1])))
'''


from math import gcd

def lcm(A, B):
    return A * B // gcd(A, B)

case = int(input(""))

for num in range(case):
    exam = input("").split(" ")
    A = int(exam[0])
    B = int(exam[1])
    print(lcm(A, B))
    
