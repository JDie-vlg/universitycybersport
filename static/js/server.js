function getCookie(name){
    let cookieValue = null;
    if (document.cookie && document.cookie !== ''){
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++){
            let cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) === (name + '=')){
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue
}
let csrftoken = getCookie('csrftoken');
function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain){
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

// $("TestedBtn").click(function (e) {
//     e.preventDefault();
//     $.ajax({
//         type: "POST",
//         url: `/start_server/${server.id}`,
//         data: {
//             id: {{ server.id }},
//             access_token: csrftoken
//         },
//         success: function(data) {
//             alert('Сервер остановлен!');
//             },
//         error: function(data) {
//             alert('Ошибка при остановке сервера!');
//             }
//     });
// });