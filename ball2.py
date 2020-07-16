def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")
    
    new_guess = []

    while len(new_guess) < 3:
        guess = input(f"{len(new_guess) + 1}번째 숫자를 입력하세요: ")
        if int(guess) < 0  or int(guess) > 9:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
        elif guess in new_guess:
            print("중복되는 숫자입니다. 다시 입력하세요.")
        else:
            new_guess.append(guess)
    
    return new_guess

print(take_guess())