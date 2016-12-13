
(function() {
  "use strict";

  $(".js-modal-login").submit(event => {
    event.preventDefault();

    $.ajax({
      method: "POST",
      url: "/login/",
      data: {
        username: $("#inputUsername3").val(),
        password: $("#inputPassword3").val(),
        csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
      },
      success: data => {
        console.log(data);
        location.reload();
      },
      error: data => {
        $(".ktowin-login-error").css('display',"block")
        console.log(data);
      }
    });
  });


})();
