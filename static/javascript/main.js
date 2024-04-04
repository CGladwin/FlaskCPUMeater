function fetch_cpu_usage(){
    $.get('api/cpu', function(data) {
        console.log(data);
        $('#cpu_usage').html(data);
        $('#progress_usage').val(data);
    })
}
setInterval(fetch_cpu_usage, 1000)

document.addEventListener("contextmenu",function(e){e.preventDefault();}, false);