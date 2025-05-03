# Task 8. Guess the number
# The program randomly guesses a number from 1 to 100.
# - The user enters guesses.
# - The program prompts "More" or "Less".
# - The game continues until the user guesses.
from random import randint

print("Hello. Let's play guess the number.")

random_number = randint(1, 100)

print(
    "I have thought of a number from 1 to 100. "
    'Try to guess it. I will prompt you "more" or "less".'
)

user_number = int(input("Guess a number from 1 to 100: "))
print(user_number)
lo_num = 1
hi_num = 100
count_tries = 1
while user_number != random_number:
    print(user_number)
    if random_number > user_number:
        lo_num = user_number
        count_tries += 1
        user_number = int(
            input(
                f"My number is higher. Try again. "
                f"Enter a number from {lo_num} to {hi_num}: "
            )
        )
    elif random_number < user_number:
        hi_num = user_number
        count_tries += 1
        user_number = int(
            input(
                f"My number is lower. Try again. "
                f"Enter a number from {lo_num} to {hi_num}: "
            )
        )

print(
    f"Congratulations! You won! You guessed my number "
    f'"{random_number}" in "{count_tries}" tries.'
)
