(function() {
  "use strict";

  $(".js-post-like").click(event => {
    event.preventDefault();
    console.log(event.target);
    console.log(event.target.getAttribute("post-id"));
    $.ajax({
      method: "POST",
      url: "/like/",
      data: {
        id: event.target.getAttribute("post-id"),
        ct: 'post',
        vote: 'like',
        csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
      },
      success: data => {
        console.log(data);
        // location.reload();
          document.getElementById(data.id).innerHTML = data.count;
      },
      error: data => {
        // $(".ktowin-login-error").css('display',"block")
        console.log(data);
      }
    });
  });


})();

(function() {
  "use strict";

  $(".js-post-dislike").click(event => {
    event.preventDefault();
    console.log(event.target);
    console.log(event.target.getAttribute("post-id"));
    $.ajax({
      method: "POST",
      url: "/like/",
      data: {
        id: event.target.getAttribute("post-id"),
        ct: 'post',
        vote: 'dislike',
        csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
      },
      success: data => {
        console.log(data);
        // location.reload();
        document.getElementById(data.id).innerHTML = data.count;

      },
      error: data => {
        // $(".ktowin-login-error").css('display',"block")
        console.log(data);
      }
    });
  });


})();

(function() {
  "use strict";

  $(".js-comment-like").click(event => {
    event.preventDefault();
    console.log(event.target);
    console.log(event.target.getAttribute("comment-id"));
    $.ajax({
      method: "POST",
      url: "/like/",
      data: {
        id: event.target.getAttribute("comment-id"),
        ct: 'comment',
        vote: 'like',
        csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
      },
      success: data => {
        console.log(data);
        // location.reload();
        document.getElementById(data.id).innerHTML = data.count;

      },
      error: data => {
        // $(".ktowin-login-error").css('display',"block")
        console.log(data);
      }
    });
  });


})();

(function() {
  "use strict";

  $(".js-comment-dislike").click(event => {
    event.preventDefault();
    console.log(event.target);
    console.log(event.target.getAttribute("comment-id"));
    $.ajax({
      method: "POST",
      url: "/like/",
      data: {
        id: event.target.getAttribute("comment-id"),
        ct: 'comment',
        vote: 'dislike',
        csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
      },
      success: data => {
        console.log(data);
        // location.reload();
        document.getElementById(data.id).innerHTML = data.count;

      },
      error: data => {
        // $(".ktowin-login-error").css('display',"block")
        console.log(data);
      }
    });
  });


})();
