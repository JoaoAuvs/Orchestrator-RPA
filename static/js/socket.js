/* CLIQUE BUTTON POST SOCKET */

$("#table-lista tbody").on("click", "button", function () {
    var button = $(this);
    var msg = button.val();
    var vm = $(this).attr("vm");
    var url = `http://${vm}:5578`;
    $.ajax({
        url: url,
        type: 'POST',
        data: { msg: msg },
        dataType: 'JSON',
        /*success: function () {
            alert(msg);
        },*/
    });
    button.prop("disabled", true); /* DESATIVA O BUTTON APÓS O CLIQUE */
});