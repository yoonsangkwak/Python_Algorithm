import random
voca = {}
with open('vocabulary.txt', 'r', encoding='UTF-8') as f:
    
    for line in f:
        data = line.strip().split(": ")
        korean = data[1]
        english = data[0]
        voca[english] = korean


while True:
    keys = list(voca.keys())
    index = random.randint(0, len(keys) - 1)
    english = keys[index]
    korean = voca[english]
    test = input(f"{korean}: ")

    if test == 'q':
        break
    elif test == english:
        print('맞았습니다!')
    else:
        print(f"아쉽습니다. 정답은 {english}입니다.")
