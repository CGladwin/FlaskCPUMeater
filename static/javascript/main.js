// function fetch_cpu_usage() {
//     $.get('api/cpu')
//         .done(function(data) {
//             console.log(data);
//             $('#cpu_usage').html(data);
//             $('#progress_usage').val(data);
//         })
//         .fail(function(jqXHR, textStatus, errorThrown) {
//             console.error('There was a problem with the fetch operation:', errorThrown);
//         });
// }

// setInterval(fetch_cpu_usage, 1000);
function fetch_cpu_usage(){
    $.get('api/cpu', function(data) {
        console.log(data);
        $('#cpu_usage').html(data);
        $('#progress_usage').val(data);
    })
}
setInterval(fetch_cpu_usage, 1000)