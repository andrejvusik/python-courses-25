# * Task 10. The longest substring
# Find the longest substring without duplicates ("abcabcbb" → "abc").

entered_string = list(input("Enter a string to find the longest substring without duplicates: "))
data_list = [[]]

num_substr = 0

while len(entered_string) > 0:
    letter = entered_string.pop(0)
    if letter not in data_list[num_substr]:
        data_list[num_substr].append(letter)
    else:
        num_substr += 1
        data_list.append([])
        data_list[num_substr].append(letter)

data_dict = {"".join(data_list[i]): len(data_list[i]) for i in range(len(data_list))}

len_max_substr = max(data_dict, key=data_dict.get)

msg = f"Longest substrings consisting of \"{data_dict[len_max_substr]}\" characters: "
for i in data_dict.keys():
    if data_dict[i] == data_dict[len_max_substr]:
        msg += f"{i}, "
print(msg[:-2] + ".")