def is_anagram(string1: str, string2: str) -> bool:
    if len(string1) != len(string2):
        return False
    string1 = sorted(string1)
    string2 = sorted(string2)
    return string1 == string2


test_string1 = 'restrain'
test_string2 = 'terrains'
print('Given Strings:\t', test_string1, ' & ', test_string2)
if is_anagram(test_string1, test_string2):
    print("Test String 1 and Test String 2 are anagrams")
else:
    print("Test String 1 and Test String 2 are not anagrams")
