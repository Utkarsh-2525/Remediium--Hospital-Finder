
let cookie = document.cookie
let csrfToken = cookie.substring(cookie.indexOf('=') + 1)
$(document).ready(function () {
    $("#submit").click(function (event) {

        event.preventDefault();
        
      var formData = {
        name: $("#disease").val(),
        
      };
      setTimeout(function(){
        $(".load").css("display", "flex");
      $.ajax({
        headers: {
            'X-CSRFToken': csrfToken
          },
        type: "POST",
        url: "REM",
        data: formData,
        csrfmiddlewaretoken: '{% csrf_token %}',
        encode: true,
        complete:(function (data) {
          $(".load").css("display", "none");
        }),
        success:(function (data) {
        $(".load").css("display", "none");
        $('#frame').attr('src',data);
      })
    });
});
  

    });
  });