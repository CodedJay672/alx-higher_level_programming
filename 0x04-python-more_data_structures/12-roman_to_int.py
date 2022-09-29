#!/usr/bin/python3
def roman_value(r):
    roman_char = r.upper()
    rom_to_int = 0
    if roman_char == 'I':
        rom_to_int = 1
    elif roman_char == 'V':
        rom_to_int = 5
    elif roman_char == 'X':
        rom_to_int = 10
    elif roman_char == 'L':
        rom_to_int = 50
    elif roman_char == 'C':
        rom_to_int = 100
    elif roman_char == 'D':
        rom_to_int = 500
    elif roman_char == 'M':
        rom_to_int = 1000
    return rom_to_int

def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    s1, s2 = 0, 0

    for i in roman_string:
        s2 = roman_value(i)
        if s2 > s1:
            s1 = s2 - s1
        else:
            s1 += s2
    return s1
