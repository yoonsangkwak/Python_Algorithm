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

def count_matching_numbers(list_1, list_2):
    count = 0
    for i in range(len(list_1)):
        for j in range(len(list_2)):
            if list_1[i] == list_2[j]:
                count += 1
    return count


def check(numbers, winning_numbers):
    correct = count_matching_numbers(numbers, winning_numbers[:6])
    bonus = count_matching_numbers(numbers, winning_numbers[6:])
    
    if correct == 6:
        price = 1000000000
    elif correct == 5 and bonus == 1:
        price = 50000000
    elif correct == 5:
        price = 1000000
    elif correct == 4:
        price = 50000
    elif correct == 3:
        price = 5000
    else:
        price = 0

    return price
