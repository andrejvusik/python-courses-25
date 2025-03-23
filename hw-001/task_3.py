# Task 3. Simplified Caesar Cipher
# Enter a lowercase Latin letter (a–z) and a number n.
# Output the letter shifted in the alphabet by n positions
# (taking into account the loop, i.e. the letter z at n=1 becomes a, at n=2 - b, etc.)

entered_character, step_cipher = input("Enter a lowercase Latin letter (a–z): "), int(input("Enter cipher step: "))

encrypted_character = chr((ord(entered_character) - 97 + step_cipher) % 26 + 97)

print("Encrypted character: ", encrypted_character)
