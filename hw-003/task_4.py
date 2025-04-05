# Task 4. The user enters a matrix (list of lists).
# Write a function that transposes the matrix without changing the input matrix.
# Matrix transposition is an operation on a matrix when its rows become columns with the same numbers.


def transposes_matrix():
    print("Enter the matrix row by row (elements separated by spaces). After entering the last row, enter \"END\"")

    count_row = 0
    count_colums = 0
    check_exit = False
    user_matrix = list()

    while not check_exit:
        user_str = input(f"Enter {count_row + 1} row of the matrix (or enter END): ")
        if user_str.upper() != "END":
            user_matrix.append(user_str.split())
            count_row += 1
            if count_colums < len(user_matrix[count_row -1]):
                count_colums = len(user_matrix[count_row -1])
        else:
            check_exit = True

    modifed_matrix = [[""] * (count_row) for _ in range(count_colums)]

    for i in range(len(user_matrix) + 1):
        for j in range(count_row):
            if i <= len(user_matrix[j]) - 1:
                modifed_matrix[i][j] = int(user_matrix[j][i])

    return(modifed_matrix)


# Checking the functionality of the function

for el in transposes_matrix():
    print(el)
