#!/usr/bin/node
const number = Number(process.argv[2]);
if (!(isNaN(number))) {
  console.log(`My number: ${number}`);
} else {
  console.log('Not a number');
}
