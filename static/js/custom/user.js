
$(function() {
    $('#file_upload').click(function() {
        var form_data = new FormData($('#form_upload')[0]);
        console.log()
        $.ajax({
            type: 'POST',
            url: '/process_file',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            async: false,
            success: function(data) {
                console.log('Success!');
            },
        });
    });
});

