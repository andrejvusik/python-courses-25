# *Task 13. Roman Numerals
# Enter a number (1-100). Convert it to the Roman system (58 → LVIII).

user_number = input("Enter a number (1-100): ")

user_number_tuple = tuple(user_number[::-1])

table_roman_tuple = (
    ("", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"),
    ("", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"),
    ("", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"),
)

roman_number = ""

for i in range(len(user_number_tuple)):
    roman_number = table_roman_tuple[i][int(user_number_tuple[i])] + roman_number

print(f"The number {user_number} in Roman numerals: {roman_number}")
