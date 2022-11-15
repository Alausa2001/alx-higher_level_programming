#!/usr/bin/node
/**
 * script that display the status code of a GET request.
 *
 * The first argument is the URL to request (GET)
 * The status code must be printed like this: code: <status code>
 * You must use the module request
 */
const req = require('request');
req.get(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
