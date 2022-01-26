/*
$(document).ready(function() {
    $("#register").click(function(event) {
        var email_address = $("#email_address").val();
        // alert("Registering: " + email_address.toString());
        $.ajax({
            data: {
                'email_address': $("#email_address").val()
            },
            type: 'POST',
            url: '/register'
        }).done(function(data) {
            if (data.status == 200) {
                alert(email_address + ' registered!');
            } else {
                alert('ERROR: ' + email_address + ' exists!');
            }
        })
    });

    $("#unregister").click(function() {
        var email_address = $("#email_address").val();
        alert("Unregistering: " + email_address.toString());
    });
});
*/

$(document).ready(function() {

    $("#register").bind('click', function() {
        $.getJSON('/register', {
            email_address: $("#email_address").val()
        }, function(data) {
            if (data.status == 200) {
                alert(email_address.value + ' registered!');
            } else {
                alert('ERROR: ' + email_address.value + ' exists!');
            }
        });
        return false;
    });

});

