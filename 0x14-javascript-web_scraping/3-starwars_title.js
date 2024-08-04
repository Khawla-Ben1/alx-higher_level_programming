#!/usr/bin/node
const re = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}/`;

re.get(url, { json: true }, (error, response, body) => {
  if (error) {
  console.error('Error:', error.message);
  return;
  }
  console.log(body.title);
});
