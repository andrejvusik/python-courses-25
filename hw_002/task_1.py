# Task 1. Count words
# The input line contains text (entered by the user).
# A word is a sequence of characters (except spaces) in a row.
# Words are separated by one or more spaces or end-of-line characters.
# Count:
# 1. How many times each word appears in the text
# and build a dictionary {word: quantity}.
# 2. The number of unique words.
# The words Apple and apple are considered the same.

users_text = input("Enter your text: ").replace("\\n", " ").lower()
list_text = users_text.split()
dict_text: dict[str, int] = dict()

for word in list_text:
    dict_text[word] = dict_text.get(word, 0) + 1

print("")
print("The line you entered contains the following number of words:")
for key in dict_text:
    print(f"  - {key}: {str(dict_text[key])} pcs.")

unique_words = {key for key in dict_text if dict_text[key] == 1}

print("")
if len(unique_words):
    print(f"The number of unique words in your text: {len(unique_words)}")
    msg = "Your unique words are: "
    for word in unique_words:
        msg += f"{word}, "
    print(msg[:-2])
else:
    print("There are no unique words!")
