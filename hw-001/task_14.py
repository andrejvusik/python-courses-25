# *Task 14. Roman arithmetic
# Enter two numbers in the Roman system (XIV, XXVIII).
# Calculate their sum and difference, returning the Roman result.

dict_roman_numbers = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

table_roman_tuple = (("", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"),
                     ("", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"),
                     ("", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"),
                     )

first_roman_number = input("Enter first roman number: ")
second_roman_number = input("Enter second roman number: ")

first_roman_number_tuple = tuple(first_roman_number)
second_roman_number_tuple = tuple(second_roman_number)

first_number_list = [dict_roman_numbers[first_roman_number_tuple[i]] for i in range(len(first_roman_number_tuple))]
second_number_list = [dict_roman_numbers[second_roman_number_tuple[i]] for i in range(len(second_roman_number_tuple))]

first_number = 0
second_number = 0

if len(first_number_list) <= 1:
    first_number += first_number_list[0]
else:
    for el in range(len(first_number_list)):
        if el == 0 and first_number_list[el] >= first_number_list[el + 1]:
            first_number += first_number_list[el]
        elif el == 0 and first_number_list[el] < first_number_list[el + 1]:
            first_number -= first_number_list[el]
        elif first_number_list[el - 1] <= first_number_list[el]:
            first_number += first_number_list[el]
        elif first_number_list[el + 1] and first_number_list[el - 1] > first_number_list[el] < first_number_list[
            el + 1]:
            first_number -= first_number_list[el]
        elif first_number_list[el + 1] and first_number_list[el - 1] > first_number_list[el] >= first_number_list[
            el + 1]:
            first_number += first_number_list[el]
        elif not first_number_list[el + 1]:
            first_number += first_number_list[el]

if len(second_number_list) <= 1:
    second_number += second_number_list[0]
else:
    for el in range(len(second_number_list)):
        if el == 0 and second_number_list[el] >= second_number_list[el + 1]:
            second_number += second_number_list[el]
        elif el == 0 and second_number_list[el] < second_number_list[el + 1]:
            second_number -= second_number_list[el]
        elif second_number_list[el - 1] <= second_number_list[el]:
            second_number += second_number_list[el]
        elif second_number_list[el + 1] and second_number_list[el - 1] > second_number_list[el] < second_number_list[
            el + 1]:
            second_number -= second_number_list[el]
        elif second_number_list[el + 1] and second_number_list[el - 1] > second_number_list[el] >= second_number_list[
            el + 1]:
            second_number += second_number_list[el]
        elif not second_number_list[el + 1]:
            second_number += second_number_list[el]

sum_of_numbers = first_number + second_number
difference_of_numbers = first_number - second_number

sum_tuple = tuple(str(sum_of_numbers)[::-1])
difference_tuple = tuple(str(abs(difference_of_numbers))[::-1])

sum_roman = ""
difference_roman = ""

for i in range(len(sum_tuple)):
    sum_roman = str(table_roman_tuple[i][int(sum_tuple[i])]) + sum_roman

for i in range(len(difference_tuple)):
    difference_roman = str(table_roman_tuple[i][int(difference_tuple[i])]) + difference_roman

if difference_of_numbers < 0:
    difference_roman = "-" + difference_roman

print("")
print("The sum of the entered numbers is:")
print(first_roman_number, "+", second_roman_number, "=", sum_roman)
print("(", first_number, " + ", second_number, " = ", sum_of_numbers, ")", sep="")
print("")
print("The difference of the entered numbers is:")
print(first_roman_number, "-", second_roman_number, "=", difference_roman)
print("(", first_number, " - ", second_number, " = ", difference_of_numbers, ")", sep="")
