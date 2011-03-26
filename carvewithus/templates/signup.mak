<%inherit file="base.mak"/>
<div class="container_12">
<div id="content" class="grid_6 push_3 content container_480">
    <div class="bar">
        <h3>Sign Up</h3>
    </div>
    <div class="sign_up_top sign_up_0">
        <fb:login-button size="xlarge">Connect Your Facebook Account</fb:login-button>
    </div>
    <div class="sign_up_1" style="display:none;">
    	<form method="post" id="signup_form_email" class="signup_form" name="signup_form_email" action="/signup/signup_post">
	    <div class="clear"></div>
	    <table class="verticalform" callpadding="0" cellspacing="0">
	        <tbody>
		   <%include file="html/signup_form.html"/>
		   <tr>
		   	<td class="label"></td>
		   	<td class="text">By clicking "Sign Up", you are agreeing to our <a href="terms">terms</a>.</td>
	           </tr>
		   <tr>
		   	<td class="label cancel_link"><a href="javascript:;" id="sign_up_with_facebook_link">Cancel</a></td>
		   	<td class="text"><a id="sign_up_button_email" href="javascript:;" class="button large red">Sign Up</a></td>
		   </tr>
		</tbody>
	    </table>
	</form>
    </div>
    <div class="sign_up_2 sign_up_top" style="display:none;">
    	<form method="post" id="signup_form_fb" class="signup_form" name="signup_form_email" action="/signup/signup_post">
	    <div class="clear"></div>
	    <table class="verticalform" callpadding="0" cellspacing="0">
	        <tbody>
		   <%include file="signup_form.html"/>
		   <tr>
		   	<td class="label"></td>
		   	<td class="text">By clicking "Sign Up", you are agreeing to our <a href="terms">terms</a>.</td>
	           </tr>
		   <tr>
		   	<td class="label"></td>
		   	<td class="text"><a id="sign_up_button_fb" href="javascript:;" class="button large red">Sign Up</a></td>
		   </tr>
		</tbody>
	    </table>
	</form>
    </div>
    <div class="sign_up_bottom sign_up_0 sign_up_2">
    	<a href="javascript:;" id="sign_up_with_email_link">Sign Up With Email</a>
    </div>
</div>
<div id="fb_preview" class="grid_2 push_3">
</div>
</div>

<div id="fb-root"></div>
<script>
    window.fbAsyncInit = function() {
        FB.init({appId: '${facebook_app_id}', status: true, cookie: true,
                 xfbml: true});
	FB.Event.subscribe('auth.login', function(response) {
            $('#content div.sign_up_0').hide();
    	    $('#content div.sign_up_1').hide();
	    $('#content div.sign_up_2').show();
	    FB.api('/me', function(response) {
	        content = '<p><a href=\"' + response.link + '\"><img src=\"http://graph.facebook.com/' + response.id +
		          '/picture?type=large\"></a></p>';
	        $('#fb_preview').html(content);
	    });
	    
	});
    };
    (function() {
        var e = document.createElement('script');
        e.type = 'text/javascript';
        e.src = document.location.protocol + '//connect.facebook.net/en_US/all.js';
        e.async = true;
        document.getElementById('fb-root').appendChild(e);
    }());
</script>
