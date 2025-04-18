# Problem 7. String compression
# The user enters a string. Write a program that compresses the string as follows:
# if the character X is repeated N times, then the resulting string should contain XN.
# Example:
# - “aaaabbbccaff”
# a4b3c2a1f2

users_string = list(input("Enter a string to compress it: "))

compression_string = list()
compression_string.append(users_string.pop(0))
compression_string.append(1)

while len(users_string) > 0:
    el = users_string.pop(0)
    if el != compression_string[-2]:
        el_count = 1
        compression_string.append(el)
        compression_string.append(el_count)
    else:
        el_count = compression_string[-1] + 1
        compression_string[-1] = el_count

print("The compressed string looks like this:", end=" ")
print("".join(str(el) for el in compression_string))
