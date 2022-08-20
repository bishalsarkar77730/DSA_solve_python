s = "PAYPALISHIRING"
numRows = 3

matrix = [[0 for i in range((len(s)))] for j in range(numRows)]

row = 0
col = 0

flow = "down"
for i in range(len(s)):
    matrix[row][col] = s[i]
    if flow == "down":
        row += 1
        if row >= numRows:
            flow = "topchangerow"
            row -= 1

    if flow == "topchangerow":
        row -= 1
        col += 1
        if row <= 0:
            row = 0
            flow = "down"

newstring = ""
for i in matrix:
    for j in i:
        if j != 0:
            newstring += j

print(newstring)
