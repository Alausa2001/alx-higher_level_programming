#!/usr/bin/python3


def roman_to_int(roman_string):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                  'C': 100, 'D': 500, 'M': 1000}
    roman_list = []
    result = 0
    if isinstance(roman_string, str):
        for sign in roman_string:
            for keys, values in roman_dict.items():
                if sign == keys:
                    roman_list.append(values)
        roman_list.append(0)

        for index in range(len(roman_list) - 1):
            if roman_list[index] < roman_list[index + 1]:
                result -= roman_list[index]
            else:
                result += roman_list[index]
        return result
    return 0
