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

$('#create_trip_1 a.btn_next').live('click', function(e){
	e.preventDefault();
	$('#create_trip_basic_form').submit();	
});

$('#create_trip_2 a.btn_next').live('click', function(e){
	e.preventDefault();
	$('#create_trip_logistics_form').submit();
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

    $('#upload_widget_btn').click(function(e){
	e.preventDefault();
    	$('input.upload_widget').show();
    });

    $('#upload_widget_cancel').click(function(e){
    	e.preventDefault();
	$('input.upload_widget').hide();
    });

    $('form.pic_upload').ajaxForm({
    	dataType: 'script'
    });
    
    /*bind enter button to form submit*/
    $('input').clickOnEnter('form a.submit');

    /*create_trip*/
    function postCreateTripForm(data) {
    	if (data.status == 1) {
	    for(var i = 1, limit = 3; i <= limit; i++) {
    	        if ( i === data.target) {
	            $('#create_trip_' + i).show();
	            $('#create_trip_menu_' + i).addClass('active');
	        } else {
	            $('#create_trip_' + i).hide();
	            $('#create_trip_menu_' + i).removeClass('active');
	        }
            } 
	}	
    }

    var create_trip_options = {
    	dataType: 'json',
	success: postCreateTripForm
    };

    $('#create_trip_basic_form').submit(function(){
    	$(this).ajaxSubmit(create_trip_options);
	return false;
    });

    $('#create_trip_logistics_form').submit(function(){
    	$(this).ajaxSubmit(create_trip_options);
	return false;
    });


    $('#add_dest_btn').click(function(e){
    	e.preventDefault();
	count = parseInt($('#itinerary_count').val());
	count++;
	element = '<tr>' + $('#itineraries-0').html().replace('>1<', '>' + count +'<').replace(/-0/g, '-' + count) + '</tr>';
	$('#itinerary-table').append(element);
	$('#itinerary_count').val(count);
    });

    /**/
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
