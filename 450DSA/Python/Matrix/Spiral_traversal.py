row1 = 4
column = 4
matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

row = 0
col = 0
result = []

while (row < row1 and col < column):
    # storing the elements of 1st row from the remaining rows, in a list.
    for i in range(col, column):
        result.append(matrix[row][i])
    row += 1
    # storing elements of last column from remaining columns, in list.
    for i in range(row, row1):
        result.append(matrix[i][column-1])
    column -= 1
    # storing the elements of last row from remaining rows, in a list.
    if (row < row1):
        for i in range(column - 1, (col - 1), -1):
            result.append(matrix[row1 - 1][i])
        row1 -= 1
    # storing elements of 1st column from remaining columns, in list.
    if (col < column):
        for i in range(row1 - 1, row - 1, -1):
            result.append(matrix[i][col])
        col += 1

print(result)
