import numpy as np


def round_to_two_decimal_places(f):
    return np.floor(f * 100.0) / 100.0


def swap_rows(matrix, row1, row2):
    matrix[[row1, row2]] = matrix[[row2, row1]]


def row_sort(matrix, m, n, k):
    for i in range(k, m):
        for g in range(i, m):
            if i != m - 1 and matrix[i][k] < matrix[g][k]:
                for j in range(n):
                    temp = matrix[i][j]
                    matrix[i][j] = matrix[g][j]
                    matrix[g][j] = temp
    return matrix


def is_upper_triangular(matrix, m):
    is_it = True
    for i in range(1, m):
        for j in range(i):
            if matrix[i][j] != 0:
                is_it = False
                break
        if not is_it:
            break
    return is_it


def get_matrix_dimensions():
    m = int(input("row: "))
    n = int(input("column: "))
    return m, n


def fill_matrix(m, n):
    matrix = np.zeros((m, n), dtype=float)
    for i in range(m):
        for j in range(n):
            matrix[i][j] = float(input(f"\tRow:{i} Column:{j}: "))
            print("\n")
    return matrix


def solve_system(matrix, m, n):
    k = 0
    while not is_upper_triangular(matrix, m):
        matrix = row_sort(matrix, m, n, k)
        copy_matrix = matrix.copy()
        pivot_element = 0

        for i in range(n):
            if copy_matrix[k][i] != 0:
                pivot_element = copy_matrix[k][i]
                break

        for i in range(k + 1, m):
            pivot_element_next_row = 0
            for g in range(n):
                if copy_matrix[i][g] != 0:
                    pivot_element_next_row = copy_matrix[i][g]
                    break
            for j in range(n):
                temp = copy_matrix[i][j] - (copy_matrix[k][j] * (pivot_element_next_row / pivot_element))
                if (0 < temp < 0.00001) or (-0.00001 < temp < 0):
                    temp = 0.0
                copy_matrix[i][j] = temp

        matrix = copy_matrix.copy()
        matrix = row_sort(matrix, m, n, k)
        k += 1

    print("\n\n")
    for i in range(m):
        for j in range(n):
            print("{:.2f}".format(matrix[i][j]), end="\t")
        print("\n")

    for i in range(m - 1, -1, -1):
        counter = 0
        for j in range(n - 1):
            if matrix[i][j] != 0:
                counter += 1
        if counter == 0 and matrix[m - 1][n - 1] != 0:
            print("Incompatible System!!!\n")
            return

    counter = 0
    is_it = True
    m1 = m - 1
    while counter == 0:
        for j in range(n - 1):
            if matrix[m1][j] != 0 and matrix[m1][n - 1] != 0:
                counter += 1
            if counter > 1:
                is_it = False
                break
        if not is_it:
            print("Compatible System with Infinite Solutions.\n")
            return
        m1 -= 1

    answer = np.zeros(n - 1)
    kk = n - 2
    # kkk = n - 2
    for i in range(m - 1, -1, -1):
        # ans = 0
        answers = np.ones(n - 1)
        for j in range(n - 1):
            answers[j] = answers[j] * matrix[i][j]
        kkk = kk
        if i == m - 1:
            answer[kk] = matrix[i][n - 1] / answers[kk]
            kk -= 1
            print("X = {:.2f}".format(answer[kkk]))
        elif i == m - 2:
            answer[kk] = (matrix[i][n - 1] - (answer[kk + 1] * matrix[i][kk + 1])) / answers[kk]
            kk -= 1
            print("X = {:.2f}".format(answer[kkk]))
        elif i == m - 3:
            answer[kk] = (matrix[i][n - 1] - (answer[kk + 1] * matrix[i][kk + 1]) - (
                    answer[kk + 2] * matrix[i][kk + 2])) / answers[kk]
            k -= 1
            print("X = {:.2f}".format(answer[kkk]))


if __name__ == "__main__":
    rows, columns = get_matrix_dimensions()
    matrix = fill_matrix(rows, columns)

    solve_system(matrix, rows, columns)
