with open('vocabulary.txt', 'r', encoding='UTF-8') as f:
    
    for line in f:
        voca = line.strip().split(": ")
        test = input(f"{voca[1]}: ")
        if test == voca[0]:
            print("맞았습니다!")
        else:
            print(f"아쉽습니다. 정답은 {voca[0]}입니다.")