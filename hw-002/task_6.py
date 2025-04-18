# Task 6. Removing duplicates without set()
# The user enters a list (any). Remove all duplicates without using set().

users_list = list(
    input("Enter any list to remove duplicates:").replace(",", " ").split()
)

users_list_without_dublicates = []
for item in users_list:
    if item not in users_list_without_dublicates:
        users_list_without_dublicates.append(item)

print("Final list without duplicates: ")
print(", ".join(users_list_without_dublicates))
