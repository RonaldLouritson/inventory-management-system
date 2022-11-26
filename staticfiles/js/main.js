$(document).ready(function () {
    $('#sanum').prop('disabled', true);
    $('#description').prop('disabled', true);
    $('#itemcategory').prop('disabled', true);
    $('#Item').prop('disabled', true);
    $('#custcontains').prop('disabled', true);
    $('#customer').prop('disabled', true);
    $('#nacontains').prop('disabled', true);
    $('#national').prop('disabled', true);
    $('#location').prop('disabled', true);
    $('#btnAdd').prop('disabled', true);
    $('#btnRemove').prop('disabled', true);
    $('#btnPrint').prop('disabled', true);
    $('#btnCopy').prop('disabled', true);
    $('#btnSave').prop('disabled', true);
    $('#btnVoid').prop('disabled', true);

    $("#btnNew").click(function () {
        $('#sanum').prop('disabled', false);
        $('#description').prop('disabled', false);
        $('#itemcategory').prop('disabled', false);
        $('#Item').prop('disabled', true);
        $('#custcontains').prop('disabled', false);
        $('#customer').prop('disabled', true);
        $('#nacontains').prop('disabled', false);
        $('#national').prop('disabled', true);
        $('#location').prop('disabled', true);
        $('#btnAdd').prop('disabled', false);

        $.ajax({
            type: "GET",
            url: 'getLoc',
            //data: {getNAccCont: $('#nacontains').val()},

            success: function (response) {
                for (var i = response.length - 1; i >= 0; i--) {
                    $("#location").append('<option>' + response[i].location + '</option>');
                };
            },
            error: function (error_response) {
                console.log("error")
            }
        });
    });

    //$('#txt1').on('input change' , function(){
    //  if($.trim($(this).val()) !== ""){
    //    $('#txt2').prop('disabled',false);
    //  }
    //});
});