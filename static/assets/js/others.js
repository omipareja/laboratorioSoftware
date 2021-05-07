$('#registerForm').on('submit', function(e) {
    e.preventDefault();
    var l = 11;
    var errors = 0;
    for (var i = 0; i < l; i++) {
       var x = document.forms["registerForm"][i].value;
       if(x == "") errors++;
    }

    if(!errors){
        $('#registro').modal('hide');
        $('#confirmacionRegistro').modal('show');  
    }

});