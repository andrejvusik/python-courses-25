# Task 4. Comparing lists of numbers
# The user enters 2 sets of numbers. Display:
# 1. Numbers that are present in both sets at the same time.
# 2. Numbers from the first set that are not present in the second, and vice versa.
# 3. Numbers from both sets, except for the numbers found in step 1.

user_numbers_set_1 = {float(number) for number in input("Enter the first list of numbers: ").split()}
user_numbers_set_2 = {float(number) for number in input("Enter the second list of numbers: ").split()}

numbers_on_both_lists = user_numbers_set_1 & user_numbers_set_2
numbers_on_only_first_list = user_numbers_set_1 - user_numbers_set_2
numbers_on_only_second_list = user_numbers_set_2 - user_numbers_set_1
numbers_on_only_first_and_second_list = user_numbers_set_1 ^ user_numbers_set_2

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
    "Numbers that are present in both sets at the same time: ",
    "There are no numbers that are present in both sets at the same time.",
    numbers_on_both_lists
)

custom_data_output(
    "Numbers from the first set that are not in the second: ",
    "There are no numbers from the first set that are not in the second.",
    numbers_on_only_first_list
)

custom_data_output(
    "Numbers from the second set that are not in the first: ",
    "There are no numbers from the second set that are not in the first.",
    numbers_on_only_second_list
)

custom_data_output(
    "Numbers from both sets except numbers present in both sets simultaneously: ",
    "There are no numbers that are present in only one set.",
    numbers_on_only_first_and_second_list
)
