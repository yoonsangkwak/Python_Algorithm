# 2476번


def func(dice):
    new_dice = sorted(dice)
    A = int(new_dice[0])
    B = int(new_dice[1])
    C = int(new_dice[2])

    if A == B == C:
        price = 10000 + A * 1000
    elif A == B < C:
        price = 1000 + A * 100
    elif A < B == C:
        price = 1000 + B * 100
    elif A < B < C:
        price = C * 100
    return price

man = int(input())
