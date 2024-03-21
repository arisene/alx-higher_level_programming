#!/usr/bin/python3

def roman_to_int(roman_string) -> int:
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                  'C': 100, 'D': 500, 'M': 1000}
    result = 0
    pre_value = 0
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    else:
        for char in reversed(roman_string):
            value = roman_dict.get(char, 0)
            if value < pre_value:
                result -= value
            else:
                result += value
            pre_value = value
        if 1 <= result <= 3999:
            return result
        else:
            return 0
