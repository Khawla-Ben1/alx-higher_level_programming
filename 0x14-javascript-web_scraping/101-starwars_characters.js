#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}/`;

function helpRequest (arr, i) {
  if (i === arr.length) {
    return;
  }
  request(arr[i], function (error, response, body) {
    if (error) {
      console.error(error);
    }
    console.log(JSON.parse(body).name);
    helpRequest(arr, i + 1);
  });
}

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const c = JSON.parse(body).characters;
  helpRequest(c, 0);
});
