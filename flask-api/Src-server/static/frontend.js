
$(document).ready(function(){


});
    $(".submit-button").on("click",function(){
    var data = new FormData();
    jQuery.each(jQuery('#file')[0].files, function(i, file) {
        data.append('file-'+i, file);
    });

    jQuery.ajax({
    url: '/image-handling',
    data: data,
    cache: false,
    contentType: false,
    processData: false,
    type: 'POST',
    success: function(data){
        alert(data);
    }

    });
});
