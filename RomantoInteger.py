def roman_to_int(s):
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    prev_value = 0

    for c in s:
        value = roman_numerals[c]
        total += value

        if value > prev_value:
            total -= 2 * prev_value

        prev_value = value

    return total

roman_numeral = "MCMXCIV"
integer_value = roman_to_int(roman_numeral)
print(f"The integer value of {roman_numeral} is {integer_value}")
