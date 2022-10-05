#!/usr/bin/node
function selectionSort (array) {
  for (let i = 0; i < array.length; i++) {
    for (let j = i + 1; j < array.length; j++) {
      let max = i;
      if (array[j] > array[max]) {
        max = j;
        if (max !== i) {
          const swap = array[i];
          array[i] = array[max];
          array[max] = swap;
        }
      }
    }
  }
  return (array);
}
const argvArr = process.argv.slice(2);
const argvIntArray = [];
for (const i of argvArr) {
  const num = parseInt(i);
  argvIntArray.push(num);
}
if (process.argv.length <= 3) {
  console.log(parseInt('0'));
} else {
  const sortedArray = selectionSort(argvIntArray);
  console.log(sortedArray[1]);
}
