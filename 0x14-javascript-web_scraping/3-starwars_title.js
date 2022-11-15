#!/usr/bin/node
const req = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
req.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const jsFormat = JSON.parse(body);
    console.log(jsFormat.title);
  }
});
