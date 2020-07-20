# 8958번

'''
case = int(input())
for num in range(case):
    quiz = input()
    i = 0
    score = 0
    bonus = 1
    while i < len(quiz) - 1:
        if quiz[i] == 'O':
            if quiz[i + 1] == 'O':
                bonus += 1
            elif quiz[i + 1] == 'X':
                bonus = 1
            score += bonus
        i += 1
    if quiz.endswith('O'):
        score += 1
    print(score)
'''

case = int(input())
for num in range(case):
    quiz = input()
    bonus = 0
    score = 0
    for i in range(len(quiz)):
        if quiz[i] == 'O':
            bonus += 1
            score += bonus
        else:
            bonus = 0
    print(score)