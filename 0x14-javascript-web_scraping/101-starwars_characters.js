#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}/`;

request(url,function (error, response, body) {
  if (error) {
    console.error('Error:', error.message);
    return;
  }
  const charactersUrls = JSON.parse(body.characters);
  if (i === charactersUrls.length) {
    return;
  }
  request(charactersUrls[i], function (error, response, body) {
    if (error) {
      console.error(error);
    }
    console.log(JSON.parse(body).name);
    helpRequest(charactersUrls, i + 1);
  });
});
