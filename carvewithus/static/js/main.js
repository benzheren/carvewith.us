/*sign up*/
$('#sign_up_with_email_link').live('click', function(){
    $('#content div.sign_up_0').hide();
    $('#content div.sign_up_2').hide();
    $('#content div.sign_up_1').show();
});

$('#sign_up_with_facebook_link').live('click', function(){
    $('#content div.sign_up_0').show();
    $('#content div.sign_up_1').hide();
});

$('#sign_up_button_email').live('click', function(){
    $('#signup_form_email').submit();
});

$('#sign_up_button_fb').live('click', function(){
    $('#signup_form_fb').submit();
});

$(document).ready(function(){
    var options = {
	    dataType: 'json',
	    success: postSignupForm
    };

    $('#signup_form_email').submit(function(){
    	$(this).ajaxSubmit(options);
	return false;
    });

    $('#signup_form_fb').submit(function(){
    	$(this).ajaxSubmit(options);
	return false;
    });
    
    /*bind enter button to form submit*/
    $("input").bind("keydown", function(event) {
    	var keycode = (event.keyCode ? event.keyCode : (event.which ? event.which : event.charCode));
      	if (keycode == 13) { 
            $('form a.submit').click();
            return false;
      	} else  {
            return true;
      	}
   }); 
    
});

function postSignupForm(data) {
    if (data.status == 1) {
    	window.location.replace(data.url);
    }
}

/*create profile*/
$('#create_profile_done').live('click', function(){
    $('#create_profile_form').submit();
    return false;
});

/*log in*/
$('#deformLogin').live('click', function(){
    $('#login_form').submit();
});
