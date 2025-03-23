# Task 2. Removing vowels
# Enter a string and remove all vowels (a, e, i, o, u) from it, then print the result.

user_string = input("Enter a string: ")
modifed_string = user_string.replace("a", "")
modifed_string = modifed_string.replace("e", "")
modifed_string = modifed_string.replace("i", "")
modifed_string = modifed_string.replace("o", "")
modifed_string = modifed_string.replace("u", "")

print("Your string without vowels: ", modifed_string)
