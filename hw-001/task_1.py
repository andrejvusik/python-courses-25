# Task 1. Formatting the full name
# Enter the last name, first name, and patronymic. Bring them to the format Last name I.O.
# (first letter of the first name and patronymic with a period).

last_name, first_name, patronymic = (
    input("What is your last name? "),
    input("What is your first name? "),
    input("What is your patronymic? "),
)

formatted_full_name = (
    last_name.capitalize()
    + " "
    + first_name[0].upper()
    + "."
    + patronymic[0].upper()
    + "."
)
print(formatted_full_name)
