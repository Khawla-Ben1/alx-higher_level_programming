#!/usr/bin/node
const fs = require('request');
const url = process.argv[2];

request.get(url, (error, response) => {
//   if (error) {
//     console.error('Error:', error.message);
//     return;
//   }
  console.log(`code: ${response.statusCode}`);
  });