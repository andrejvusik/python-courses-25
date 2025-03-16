# Task 8. Palindrome
# Enter a string and determine whether it is a palindrome
# (reads the same from left to right and from right to left).

test_string = input("Enter a string to check if it is a palindrome: ")

reverse_test_string = test_string[::-1]

if test_string == reverse_test_string:
    print(f"The entered string \"{test_string}\" is a palindrome!")
else:
    print(f"The entered string \"{test_string}\" is NOT a palindrome!")

