# * Task 9. Caesar Cipher
# The user enters a string and a number N (can be either positive or negative).
# Write a program that encrypts the string using the Caesar Cipher.
# The Caesar Cipher is a substitution cipher where each letter in the
# original text is shifted up or down the alphabet by N positions.
# Example:
# Enter N: 3
# Enter text: hello
# Result: khoor
# Explanation:
# In the word hello, each letter is shifted by 3 positions in the alphabet.
# Thus, h becomes k (alphabet a b c d e f g h i j k l m n o p q r s t u v w x y z),
# e becomes h, l becomes o, o becomes r.

step_cipher = int(input("Enter cipher step: "))
entered_string = input("Enter a string of lowercase Latin letters (a–z): ").lower()

def encrypted_character(character, step):
    if character == " ":
        return " "
    else:
        encr_character = chr((ord(character) - 97 + step) % 26 + 97)
        return encr_character

encrypted_string = [encrypted_character(character, step_cipher) for character in entered_string]

print("Encrypted string: ", end="")
print("".join(encrypted_string))


