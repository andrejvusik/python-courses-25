# Task 4. The user enters a matrix (list of lists).
# Write a function that transposes the matrix without changing the input matrix.
# Matrix transposition is an operation on a matrix when its rows become columns with the same numbers.
from itertools import count


def input_matrix(matrix=None):
    if matrix is None:
        user_matrix = input("Enter the matrix of numbers (in list of lists format): ")
        user_matrix = (
            user_matrix.strip("[]()")
            .replace(" ", "")
            .replace("),(", ";")
            .replace("],[", ";")
            .split(";")
        )
        result_matrix = []
        for i in range(len(user_matrix)):
            result_matrix.append([])
            for j in user_matrix[i].split(","):
                if j:
                    result_matrix[i].append(int(j))
                else:
                    result_matrix[i].append(0)
    else:
        result_matrix = matrix
    count_rows = len(result_matrix)
    count_cols = len(result_matrix[0])
    for i in range(1, count_rows):
        if len(result_matrix[i]) > count_cols:
            count_cols = len(result_matrix[i])
    return result_matrix, count_rows, count_cols

def transposes_matrix(matrix=None):
    matrix_after, cnt_rows, cnt_cols = input_matrix(matrix)
    matrix_before = [[0] * cnt_rows for _ in range(cnt_cols)]
    for i in range(len(matrix_after) + 1):
        for j in range(cnt_rows):
            if i <= len(matrix_after[j]) - 1:
                matrix_before[i][j] = matrix_after[j][i]
    return matrix_before



# Checking the functionality of the function

print(transposes_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(transposes_matrix())
