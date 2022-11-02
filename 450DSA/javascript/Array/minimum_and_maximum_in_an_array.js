const A = [3, 2, 1, 56, 10000, 167];
const N = A.length;

// ---------------------------- USING LOOP METHOD ----------------------
//  First make two blank array with initial value 0 to store the previous data

let mini = A[0];
let maxi = A[0];

for (let i = 1; i < N; ++i) {
  if (A[i] > maxi) {
    maxi = A[i];
  }
  if (A[i] < mini) {
    mini = A[i];
  }
}

console.log("Minimum Value = ", mini);
console.log("Maximum value = ", maxi);