# Task 3. The Second Largest Number
# The user enters a list of numbers. Find the second largest number.

user_numbers_list = [
    float(number) for number in input("Enter a list of numbers: ").split()
]

# for _ in range(user_numbers_list.count(max(user_numbers_list))):
#     user_numbers_list.remove(max(user_numbers_list))

# Alternative option based on "while"
max_number = max(user_numbers_list)
while max_number in user_numbers_list:
    user_numbers_list.remove(max(user_numbers_list))

second_largest_number = (
    int(max(user_numbers_list))
    if not max(user_numbers_list) % 1
    else max(user_numbers_list)
)

print(f"The second largest number in your list of number: {second_largest_number}")
