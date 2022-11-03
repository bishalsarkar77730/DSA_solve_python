const arr = [7, 10, 4, 20, 15];
const K = 4;
arr.sort(function (a, b) {
  return a - b;
});
let result = [];
for (let i = 0; i < K; ++i) {
  result.push(arr[i]);
}
console.log(result.at(-1));
