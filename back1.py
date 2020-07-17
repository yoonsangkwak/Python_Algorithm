def add_AB():
    while True:
        try:
            A = input("0보다 크고 10보다 작은 정수(A)를 입력하세요: ")
            num_A = int(A)
            if num_A > 0 and num_A < 10:
                B = input("0보다 크고 10보다 작은 정수(B)를 입력하세요: ")
                num_B = int(B)
                if num_B > 0 and num_B < 10:
                    answer = num_A + num_B
                    print(answer)
            else:
                print("0보다 크고 10보다 작은 정수를 입력하세요.")
        except ValueError:
            print("숫자를 입력하세요.")

add_AB()