#!/usr/bin/node
const req = require('request');
const obj = {};
req(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const jsFormat = JSON.parse(body);
    for (const x of jsFormat) {
      if (!(x.userId in obj) && x.completed === true) {
        obj[x.userId] = 1;
      } else if (x.userId in obj && x.completed === true) {
        obj[x.userId] += 1;
      }
    }
  }
  console.log(obj);
});
