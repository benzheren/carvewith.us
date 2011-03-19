$('#sign_up_with_email_link').live('click', function(){
    $('#sign_up div.sign_up_0').hide();
    $('#sign_up div.sign_up_2').hide();
    $('#sign_up div.sign_up_1').show();
})

$('#sign_up_with_facebook_link').live('click', function(){
    $('#sign_up div.sign_up_0').show();
    $('#sign_up div.sign_up_1').hide();
});
