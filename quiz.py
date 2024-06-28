def reverse_list(l: list):
    """
TODO: Reverse a list without using any built in functions

The function should return a sorted list.
Input l is a list which can contain any type of data.
"""
    list_len = len(l) - 1
    start = 0
    while start <= list_len:
        temp = l[start]
        l[start] = l[list_len]
        l[list_len] = temp
        list_len -= 1
        start += 1


pass
mylist = [1, 2, 4, -1, 0, 3, 4]
reverse_list(mylist)
print(mylist)


def validate(row, colNum, matrix, i):
    # validation for each row
    for index in range(0, 9):
        if row[index] == i:
            return False

    # validation for each col
    for row in matrix:
        if row[colNum] == i:
            return False

    return True
    pass


def backTracking(matrix):
    for row in matrix:
        for col in row:
            colNum = row.index(col)
            # if there is a number then come to next position
            if col != 0:
                continue

            for i in range(1, 10):
                # validate the numbers from 1-9, if there is a valid number, put in,
                # or error(cause it can't satisfy the requirement, then the matrix is not a valid sudoku)
                if validate(row, colNum, matrix, i):
                    row[colNum] = i
                    # put in the number, and come to next point, repeat them once again
                    bo = backTracking(matrix)
                    if bo:
                        return True
                    # if the backtracking return false, means that the data has error
                    # then we should return to previous step and withdraw the data,
                    # and continue to next number(1-9) if it has
                    else:
                        row[colNum] = 0

        return False
    return True
    pass


def solve_sudoku(matrix):
    """TODO: Write a programme to solve 9x9 Sudoku board.

    Sudoku is one of the most popular puzzle games of all time. The goal of Sudoku is to fill a 9×9 grid with numbers so that each row, column and 3×3 section contain all of the digits between 1 and 9. As a logic puzzle, Sudoku is also an excellent brain game.

    The input matrix is a 9x9 matrix. You need to write a program to solve it.
 """
    bo = backTracking(matrix)
    return bo
    pass


matrix = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 5, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 7, 9]]

if solve_sudoku(matrix):
    for index in matrix:
        print(index)
else:
    print("it is not a valid sudoku")
