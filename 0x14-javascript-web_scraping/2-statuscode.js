#!/usr/bin/node
const re = require('request');
const url = process.argv[2];

re.get(url, (error, response) => {
  if (error) {
    console.error('Error:', error.message);
    return;
  }
  console.log(`code: ${response.statusCode}`);
  });
