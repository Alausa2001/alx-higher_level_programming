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
const arr = process.argv.slice(2);
const intArray = [];
for (const i of arr) {
  const num = parseInt(i);
  intArray.push(num);
}
if (process.argv.length <= 3) {
  console.log(parseInt('0'));
} else {
  const sortedArray = selectionSort(intArray);
  console.log(sortedArray[1]);
}
