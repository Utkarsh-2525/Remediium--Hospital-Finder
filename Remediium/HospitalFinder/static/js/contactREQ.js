
let cookie = document.cookie
let csrfToken = cookie.substring(cookie.indexOf('=') + 1)
$(document).ready(function () {
    $("#submit").click(function (event) {

        event.preventDefault();
        
      var formData = {
        name: $("#search").val(),
        
      };
  
      $.ajax({
        headers: {
            'X-CSRFToken': csrfToken
          },
        type: "POST",
        url: "REM",
        data: formData,
        csrfmiddlewaretoken: '{% csrf_token %}',
        encode: true,
      }).done(function (data) {
        
        $('html').html('<div id="wrapper" class="animated zoomIn"> <h1> <!-- The <h1> tag is the reason why the text is big! --> <underline>Thank you!</underline> <!-- The underline makes a border on the top and on the bottom of the text --></h1><h3>For reaching to us!</h3></div><style>@mixin vertical-align($position: relative) { position: $position; top: 50%; -webkit-transform: translateY(-50%); -ms-transform: translateY(-50%); transform: translateY(-50%);}body, html { background: #16A085;}#wrapper { width: 600px; margin: 0 auto; margin-top: 15%;}h1 { color: #EEE; text-shadow: -1px -2px 3px rgba(17, 17, 17, 0.3); text-align: center; font-family: "Monsterrat", sans-serif; font-weight: 900; text-transform: uppercase; font-size: 80px; margin-bottom: -5px;}h1 underline { border-top: 5px solid rgba(26, 188, 156, 0.3); border-bottom: 5px solid rgba(26, 188, 156, 0.3);}h3 { width: 570px; margin-left: 16px; font-family: "Lato", sans-serif; font-weight: 600; color: #EEE;}</style>');
        
      });
  
      
    });
  });