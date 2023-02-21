$("DIV#toggle_header").click(function () {
  $(this).toggleClass(function () {
          if ($(this).hasClass("red"))
                  return "green";
          else
                  return "red";
  });
});
