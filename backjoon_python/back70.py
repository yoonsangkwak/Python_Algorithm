# 4344번

case = int(input())

for i in range(case):
    score = list(map(int, input().split()))
    student = score[0]
    score = score[1:]
    even = 0
    good_student = []
    
    for j in range(len(score)):
        even += score[j]
    even = even / len(score)

    for k in range(len(score)):
        if score[k] > even:
            good_student.append(score[k])
    
    answer = round(len(good_student) / len(score) * 100, 3)
    print(f"{format(answer, '.3f')}%")