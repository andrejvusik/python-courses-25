# Task 2. Analyzing a list of numbers
# The user enters a list of numbers.
# The numbers are entered separated by a space, and can be
# both integers and floating point numbers.
# Display on the screen:
# 1. Unique numbers.
# 2. Repeating numbers.
# 3. Even and odd numbers.
# 4. Negative numbers.
# 5. Floating point numbers.
# 6. The sum of all numbers multiple of 5.
# 7. The largest number.
# 8. The smallest number.

user_numbers_list = [
    float(number) for number in input("Enter a list of numbers: ").split()
]

unique_number_list = [
    number for number in user_numbers_list if user_numbers_list.count(number) == 1
]

repeating_number_list = {
    number for number in user_numbers_list if user_numbers_list.count(number) > 1
}

even_number_list = {
    number for number in user_numbers_list if not number % 1 and not number % 2
}
odd_number_list = {
    number for number in user_numbers_list if not number % 1 and number % 2
}

negative_number_list = {number for number in user_numbers_list if number < 1}

floating_point_number_list = {number for number in user_numbers_list if number % 1}

sum_numbers_multiple_of_five = 0
for number in user_numbers_list:
    if number % 5 == 0:
        sum_numbers_multiple_of_five += int(number)

largest_number = (
    int(max(user_numbers_list))
    if not max(user_numbers_list) % 1
    else max(user_numbers_list)
)

smallest_number = (
    int(min(user_numbers_list))
    if not min(user_numbers_list) % 1
    else min(user_numbers_list)
)


def custom_data_output(msg_1, msg_2, list_number):
    if len(list_number):
        for number in list_number:
            if not number % 1:
                number = int(number)
            msg_1 += str(number) + ", "
        print(msg_1[:-2])
    else:
        print(msg_2)


custom_data_output(
    "Unique numbers from your set of numbers: ",
    "There are no unique numbers in your list of numbers!",
    unique_number_list,
)

custom_data_output(
    "Repeating numbers from your set of numbers: ",
    "There are no repeating numbers in your list of numbers!!",
    repeating_number_list,
)

custom_data_output(
    "Even numbers from your set of numbers: ",
    "There are no even numbers in your list of numbers!",
    even_number_list,
)

custom_data_output(
    "Odd numbers from your set of numbers: ",
    "There are no odd numbers in your list of numbers!",
    odd_number_list,
)

custom_data_output(
    "Negative numbers from your set of numbers: ",
    "There are no negative numbers in your list of numbers!",
    negative_number_list,
)

custom_data_output(
    "Floating point numbers from your set of numbers: ",
    "There are no floating point numbers in your list of numbers!",
    floating_point_number_list,
)

if sum_numbers_multiple_of_five:
    print(f"The sum of all numbers multiple of 5: {sum_numbers_multiple_of_five}")
else:
    print("There are no numbers multiple of 5 in your list of numbers!")

print(f"The largest number: {largest_number}")
print(f"The smallest number: {smallest_number}")
