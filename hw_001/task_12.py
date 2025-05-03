# *Task 12. Number system
# Enter a number in decimal. Convert it to binary, and then
# back to decimal, without using the built-in functions bin() and int().

user_entered_number = int(input("Enter a number in decimal: "))

str_number_bin = ""
entered_number = user_entered_number

while entered_number > 0:
    str_number_bin += str(entered_number % 2)
    entered_number //= 2

str_number_bin = str_number_bin[::-1]

print(
    f"The entered decimal number {user_entered_number} "
    f"in binary notation: {str_number_bin}"
)

number_dec = 0
power_of_number = len(str_number_bin) - 1
for i in str_number_bin:
    number_dec += int(i) * 2**power_of_number
    power_of_number -= 1

print(f"The binary number {str_number_bin} " f"in decimal notation: {number_dec}")
