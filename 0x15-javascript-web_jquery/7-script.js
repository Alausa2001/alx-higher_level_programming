$.get(
    'https://swapi-api.hbtn.io/api/people/5/?format=json',
    function (data, status) {
        $('DIV#character').append('<li>'+ data.name +'</li>')
    },
    'json'
);