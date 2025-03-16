# Task 6. Magic number
# Enter a number and calculate the sum of its digits.
# If the number is divisible by 7 without a remainder, print "Magic number!",
# otherwise just the sum of the digits.
from more_itertools.recipes import sum_of_squares

user_number = input("Enter a number: ")

if int(user_number) % 7 == 0:
    print("Magic number!")

else:
    sum_of_digits = 0
    for i in user_number:
        sum_of_digits += int(i)

    print(f"The sum of the digits of the number {user_number} is:", sum_of_digits)