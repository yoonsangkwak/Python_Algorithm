# 2231번

N = int(input())
M = 0

def get_divided_num(x): # 무차별로 대입할 생성자(x)을 분해해서 분해합을 만듬
    n = list(map(int, str(x)))  # x값이 abc라면 a, b, c로 분해해서 int로 변환
    divided_num = x + sum(n)    # 원래값과 분해한 수들의 합을 더한다
    return divided_num  


while get_divided_num(M) != N:  # 분해합을 구해서 주어진 분해합과 같지않다면 계속 반복
    if M == N:  # 만약 1씩 더해가며 분해합과 같은 수에까지 도달했다면, 분해합에 대한 생성자가
                # 없다는 뜻이므로 M에 0을 대입하고 루프문을 빠져나온다.
        M = 0
        break
    else:
        M += 1  # M값을 1씩 더해가면서 주어진 부해합과 같은 값이 나올때까지 반복

print(M)