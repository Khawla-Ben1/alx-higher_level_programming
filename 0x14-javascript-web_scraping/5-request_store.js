#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const filePath = process.argv[3];

request.get(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  fs.writeFile(filePath, body, 'utf8', (err) => {
      if (err) {
        console.error('Error writing file:', err);
      }
    });
});
