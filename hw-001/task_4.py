# Task 4. Checking the password
# Enter the password, check it, and display on the screen:
# - If less than 16 characters → "Too short"
# - If it contains only letters or only numbers → "Weak password"
# - Otherwise → "Strong password".

user_password = input("Enter your password: ")
if len(user_password) < 16:
    print("Your password is too short")
elif user_password.isdigit() or user_password.isalpha():
    print("Your password is too weak")
else:
    print("Your password is quite strong. ")
