$.get(
    'https://swapi-api.hbtn.io/api/films/?format=json',
    function (movies, status) {
        $.each(movies.results, function (index, movie)
        {
            $('UL#list_movies').append('<li>'+ movie.title +'</li>')
        });
    }
);