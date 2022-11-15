#!/usr/bin/node
const fs = require('fs');
const Buf = Buffer.alloc(1024);
fs.open(process.argv[2], 'r', function (err, file) {
  if (err) {
    console.error(err);
  } else {
    fs.read(file, Buf, 0, Buf.length, 0, function (err, bytes, content) {
      if (err) {
        console.log(err);
      }
      console.log(content.toString());
    });
  }
});
