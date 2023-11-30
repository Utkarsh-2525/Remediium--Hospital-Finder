let cookie = document.cookie
let csrfToken = cookie.substring(cookie.indexOf('=') + 1)
$(document).ready(function () {
    $("#submit").click(function (event) {

        event.preventDefault();

        var formData = {
            symptom: $("#symptom").val(),
            city: $("#city").val()

        };
        setTimeout(function () {
            $(".load").css("display", "flex");
            $.ajax({
                headers: {
                    'X-CSRFToken': csrfToken
                },
                type: "POST",
                url: "REQ",
                data: formData,
                csrfmiddlewaretoken: '{% csrf_token %}',
                encode: true,
                complete: (function (data) {
                    $(".load").css("display", "none");
                }),
                success: (function (data) {
                    $(".load").css("display", "none");
                    const arr = JSON.parse(data)
                  Console.log(arr)
                    for (let i = 0; i < arr.length; i++) {
                        $('body').append("<center><div class='data'> <h2>" + arr[i] + "</h2> <button class='searchmaps' OnClick=' location.href='https://www.google.com/maps/search/" + arr[i] + "''>Search On Maps</button> </div></center>" +
                            "<style> .data{ margin-bottom:10px; width:80%; padding:10px; display: flex; justify-content: space-between; align-items: center; background:#fff; border-radius: 5px; } h2{ color:#1a1a1a; font-size:20px; font-weight:200; display: inline; padding:10px; } .searchmaps{ padding:10px; height:50px; width:200px; " +
                            "border:1px solid #1a1a1a; " +
                            "" +
                            "background:linear-gradient(245.59deg, #4d9559 0%, #38703d 28.53%, #133917 75.52%); color:#fff; border-radius:5px; }</style>");
                    }
                })
            });
        });


    });
});