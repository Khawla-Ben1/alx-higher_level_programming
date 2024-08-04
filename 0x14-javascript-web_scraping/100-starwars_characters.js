#!/usr/bin/node
const request = require('request');

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}/`;

request(url, { json: true }, (error, response, body) => {
  if (error) {
    console.error('Error:', error.message);
    return;
  }
  const charactersUrls = body.characters;
  const fetchCharacterNames = (urls) => {
    urls.forEach(characterUrl => {
      request(characterUrl, { json: true }, (error, response, body) => {
        if (error) {
          console.error('Error:', error.message);
          return;
        }
        console.log(body.name);
      });
    });
  };
  fetchCharacterNames(charactersUrls);
});
