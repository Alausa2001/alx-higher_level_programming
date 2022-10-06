#!/usr/bin/node
exports.esrever = function (list) {
  let count;
  for (count = 0; count < list.length - 1; count++);
  const newList = [];
  while (count >= 0) {
    newList.push(list[count]);
    count--;
  }
  if (list.length === 0) {
    return ([]);
  }
  return (newList);
};
