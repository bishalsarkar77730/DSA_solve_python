let r = 4;
let c = 4;
let matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12],
  [13, 14, 15, 16],
];

let row = 0;
let col = 0;
let result = [];

while (row < r && col < c) {
  for (let i = col; i < c; i++) result.push(matrix[row][i]);
  row++;
  for (let i = row; i < r; i++) result.push(matrix[i][c - 1]);
  c--;
  if (row < r) {
    for (let i = c - 1; i >= col; --i) result.push(matrix[r - 1][i]);
    r--;
  }
  if (col < c) {
    for (let i = r - 1; i >= row; --i) result.push(matrix[i][col]);
    col++;
  }
}
console.log(result);
