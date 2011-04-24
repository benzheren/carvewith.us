/*sign up*/
$('#sign_up_with_email_link').live('click', function(){
    $('#content div.sign_up_0').hide();
    $('#content div.sign_up_2').hide();
    $('#fb_preview').hide();
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

$('#create_trip_form a.btn_next').live('click', function(e){
    e.preventDefault();
    var target = parseInt($(this).attr('alt'));
    for(var i = 1, limit = 3; i <= limit; i++) {
    	if ( i === target) {
	    $('#create_trip_' + i).show();
	    $('#create_trip_menu_' + i).addClass('active');
	} else {
	    $('#create_trip_' + i).hide();
	    $('#create_trip_menu_' + i).removeClass('active');
	}
    }
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
    $('input').clickOnEnter('form a.submit');
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
$('#login_btn').live('click', function(){
    $('#login_form').submit();
    return false;
});

/*create trip*/
$('#create_trip_btn').live('click', function(e){
    e.preventDefault();
    $('#create_trip_form').submit();
})
