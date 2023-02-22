const $ul = $("UL#list_movies");
$.get("https://swapi-api.alx-tools.com/api/films/?format=json", function (data, textStatus) {
  $.each(data.results, function (i, item) {
    $ul.append('<li>' + item.title + '</li>');
  });
});
