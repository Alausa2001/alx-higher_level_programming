#!/usr/bin/node
const list = require('./100-data').list;
const newList = list.map((x, index) => index * x);
console.log(list);
console.log(newList);
