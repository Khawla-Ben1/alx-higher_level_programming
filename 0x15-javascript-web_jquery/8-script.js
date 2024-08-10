// fetches and lists the title for all movies by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json
$.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
    const movies = data.results;
    movies.forEach(function(movie) {
        $('#list_movies').append('<li>' + movie.title + '</li>');
    });
});
