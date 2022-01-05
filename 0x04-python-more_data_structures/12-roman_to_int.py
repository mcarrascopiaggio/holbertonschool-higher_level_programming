#!/usr/bin/python3
def roman_to_int(roman_string):
    rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if type(roman_string) == str:
        res = 0
        for i in roman_string:
            if i == rom_val.keys[i]:
                res = res + rom_val.values[i]
            return res
    else:
        return 0
