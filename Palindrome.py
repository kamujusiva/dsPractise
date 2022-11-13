def reverse(given_array: list) -> list:
    start_position = 0
    end_position = len(given_array) - 1
    while end_position > start_position:
        given_array[start_position], given_array[end_position] = given_array[end_position], given_array[start_position]
        start_position = start_position + 1
        end_position = end_position - 1
    return given_array


def is_palindrome(given_str: str) -> bool:
    given_str = list(given_str)
    if given_str == reverse(given_str):
        return True
    return False


test_string = 'rotator'
print('Given String:\t', test_string)
if is_palindrome(test_string):
    print("Test String is Palindrome")
else:
    print("Test String is not Palindrome")
