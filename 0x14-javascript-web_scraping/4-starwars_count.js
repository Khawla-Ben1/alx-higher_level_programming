#!/usr/bin/node
const re = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/18/`;

re.get(url, { json: true }, (error, response, body) => {
  if (error) {
    console.error('Error:', error.message);
    return;
  }
  const movies = body.results;
  const count = movies.filter(movie =>
    movie.characters.some(character => character.endsWith(`/${wedgeAntillesId}/`))
  ).length;
});
