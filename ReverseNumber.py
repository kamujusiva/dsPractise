import math


def number_reversal(given_number: int) -> int:
    if given_number == 0:
        return 0
    reversed_number = 0
    while given_number > 0:
        reversed_number = (reversed_number * 10) + (given_number % 10)
        given_number = math.floor(given_number / 10)
    return reversed_number


test_number = 4568
print('Test Number:\t\t', test_number)
print('Reversed Number:\t', number_reversal(test_number))
