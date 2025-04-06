# Task 9. Comparing fractional numbers
# Enter two floating-point numbers.
# Print True if their difference in absolute value is less than 0.001, otherwise False.

first_float_number = float(input("Enter first float number: "))
second_float_number = float(input("Enter second float number: "))

print(abs(first_float_number - second_float_number) < 0.001)