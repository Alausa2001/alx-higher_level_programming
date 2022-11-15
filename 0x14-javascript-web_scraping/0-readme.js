#!/usr/bin/node
const fs = require('fs');
fs.readFile(process.argv[2], function (err, data) {
  if (err) {
    console.error(err);
  } else {
    console.log(data.toString());
  }
});
