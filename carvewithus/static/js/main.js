$('#sign_up_with_email_link').live('click', function(){
    $('#content div.sign_up_0').hide();
    $('#content div.sign_up_2').hide();
    $('#content div.sign_up_1').show();
})

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
});

function postSignupForm(data) {
    if (data.status == 1) {
    	window.location.replace(data.url);
    }
}


