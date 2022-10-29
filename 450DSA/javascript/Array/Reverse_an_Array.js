const A = [1,2,3,4]

// inbuilt function method
A.reverse()

// loop method

function reverseArray(arr) {
  var newArr = [];
  for (var i = 0, B = arr.length - 1; i < arr.length; i++, B--) {
    newArr[i] = arr[B];
  }
  return newArr;
}

console.log(reverseArray(A));