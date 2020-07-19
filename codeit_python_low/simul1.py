import random

answer = random.randint(1, 20)
num_tries = 4
tries = 0
chance = 0


while chance != answer and tries < num_tries:
    chance = int(input(f"기회가 {num_tries - tries}번 남았습니다. 1-20 사이의 숫자를 맞춰 보세요: "))
    tries += 1

    if chance > answer:
        print("DOWN")
    elif chance < answer:
        print("UP")

if chance == answer:
    print(f"축하합니다. {tries}번 만에 숫자를 맞추셨습니다.")
else:
    print(f"아쉽습니다. 정답은{answer}입니다.")