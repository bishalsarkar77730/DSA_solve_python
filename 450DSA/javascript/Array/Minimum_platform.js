const arr = [0900, 0940, 0950, 1100, 1500, 1800];
const dep = [0910, 1200, 1120, 1130, 1900, 2000];
const n = arr.length;
let Trains = [];
for (let i = 0; i < n; i++) {
  Trains.push([arr[i], 0]);
  Trains.push([dep[i], 1]);
}
Trains.sort(function (a, b) {
  if (a[0] == b[0]) return a[1] - b[1];
  return a[0] - b[0];
});

let result = 1;
let Needed_platform = 0;
let Loop_runs = 0;

for (; Loop_runs < Trains.length; Loop_runs++) {
  if (Trains[Loop_runs][1] == 0) Needed_platform++;
  else Needed_platform--;
  if (Needed_platform > result) result = Needed_platform;
}
console.log(result);
