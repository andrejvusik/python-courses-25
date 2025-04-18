# Task 5. Anagrams
# The user enters 2 words.
# Write a program that checks whether they are anagrams
# (the first word can be formed by rearranging the letters in the second word).
# Example:
# - “listen”
# - “silent”
# True

print("This is an anagram check.")
first_word = input("Enter a first word: ").lower()
second_word = input("Enter a first word: ").lower()

first_word_list = list(first_word)
second_word_list = list(second_word)

first_word_list.sort()
second_word_list.sort()

if first_word_list == second_word_list:
    print(
        f'True! The words you entered "{first_word}" and "{second_word}" are anagrams!'
    )
else:
    print(
        f'False! The words you entered "{first_word}" and "{second_word}" are NOT anagrams!'
    )
