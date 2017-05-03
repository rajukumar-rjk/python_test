

$(document).ready(function(){
    console.log ('loaded');

    $(document).on('submit','#register-form',function(e){
        e.preventDefault();
        console.log ('form submitted');

        var form = $('#register-form').serialize()
        $.ajax({

            type: "POST",
            url: '/postregistration',
            data: form,
            success: function(response){
            console.log(response);
            }
        })
    });

    $(document).on('submit','#login-form',function(e){
        e.preventDefault();

        var form = $('#login-form').serialize()
        $.ajax({
            type: 'POST',
            url: '/checklogin',
            data: form,
            success: function(res){
                if (res == "error"){
                    alert('Couldnt login')
                }else{
                    console.log('Logged in as',res);

                    document.location.href = '/',true;
                }
            }
        })
    });
    $(document).on('click','#logout-link',function(e){

        e.preventDefault();
        $.ajax({
            url: '/logout',
            type: 'GET',
            success: function(res){
                if (res =='sucess'){
                    document.location.href ='/login',true;
                }else{

                    alert('somthing went wrong');
                }

            }

        })
    });
});