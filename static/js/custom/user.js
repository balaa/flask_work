
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
            success: function(res) {
                json_values = res['data']
                $.each(json_values, function(key, value) {
                    $("[id$=choice]").append('<option value="' +  value + '">' +  value + '</option>');
                });
            },
        });
    });
});

