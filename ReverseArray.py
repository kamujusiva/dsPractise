import numpy as np


def reverse(given_array: list) -> list:
    start_position = 0
    end_position = len(given_array) - 1
    while end_position > start_position:
        given_array[start_position], given_array[end_position] = given_array[end_position], given_array[start_position]
        start_position = start_position + 1
        end_position = end_position - 1
    return given_array


test_array = np.array([1, 2, 3, 4, 5, 6, 7])
print('Given Array:\t', test_array)
print('Reversed Array:\t', reverse(test_array))
