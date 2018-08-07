$("#upload").click(function () {
    $.ajax({
        url: /upload/,
        type: 'POST',
        data: new FormData($("#uploadForm")[0]),
        processData: false,
        contentType: false,
        success: function (response, status, xhr) {
            alert(response);
        },
        timeout: 6000
    });
});
