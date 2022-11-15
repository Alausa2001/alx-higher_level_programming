#!/usr/bin/node
const req = require('request');
req.get(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const characters = [];
    const jsFormat = JSON.parse(body);
    for (let i = 0; i < 7; i++) {
      characters.push(jsFormat.results[i].characters);
    }
    let count = 0;
    for (let i = 0; i < characters.length; i++) {
      for (const j of characters[i]) {
        if (j === 'https://swapi-api.hbtn.io/api/people/18/') { count += 1; }
      }
    }
    console.log(count);
  }
});
