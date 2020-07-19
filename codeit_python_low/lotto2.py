from random import randint


def generate_numbers(n):
    numbers = []
    while len(numbers) < n:
        num = randint(1, 45)
        if num not in numbers:
            numbers.append(num)
    return numbers


def draw_winning_numbers():
    winning_numbers = generate_numbers(6)
    winning_numbers.sort()

    while len(winning_numbers) < 7:
        num = randint(1, 45)
        if num not in winning_numbers:
            winning_numbers.append(num)
        

    return winning_numbers


print(generate_numbers(6))
print(draw_winning_numbers())
