import random


def find_max(numbers):
    max = numbers[0]
    for number in numbers:
        if number > max:
            max=number
    return max


class Dice:
    def roll():
        first_number = random.randint(1,6)
        second_number = random.randint(1,6)
        return first_number, second_number
