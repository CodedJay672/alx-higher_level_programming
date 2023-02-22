$('document').ready(function () {
	const url = 'https://www.fourtonfish.com/hellosalut/hello/';
	$('INPUT#btn_translate').on('click', function () {
		$.get(url + $.param({lang: $('INPUT#language_conde').val()}), function (data) {
			$('DIV#hello').html(data.hello);
		});
	});
});
