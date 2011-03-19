<%inherit file="base.mak"/>
<div class="container_12">
<div class="grid_6 prefix_3 suffix_3">
<div id="sign_up" class="content">
    <div class="title content">
        Sign up
    </div>
    <div class="top sign_up_0">
        <fb:login-button size="xlarge">Connect Your Facebook Account</fb:login-button>
    </div>
    <div class="sign_up_1" style="display:none;">
	<form method="post">
            ${fs.render()}
	    <input type="checkbox" id="allow_passwordless" value="allow_passwordless" name="allow_passwordless" checked="checked">
	    <label for="allow_passwordless" class="login_option">Let me login without a password on this browser</label>
	    <a href="#" id="sign_up_with_facebook_link">Cancel</a>
	    <input type="submit" value="save">
        </form>
    </div>
    <div class="sign_up_2 top" style="display:none;">
	<form method="post">
            ${fs.render()}
	    <input type="checkbox" id="" value="allow_passwordless" name="allow_passwordless" checked="checked">
	    <label for="_allow_passwordless" class="login_option">Let me login without a password on this browser</label>
	    <input type="submit" value="save">
        </form>
    </div>
    <div class="bottom sign_up_0 sign_up_2">
        <a href="#" id="sign_up_with_email_link">Sign Up With Email</a>
    </div>
</div>
</div>
</div>

% if id:
    <p><a href="${profile_url}"><img src="http://graph.facebook.com/${id}/picture?type=square"/></a></p>
% endif



<div id="fb-root"></div>
<script>
    window.fbAsyncInit = function() {
        FB.init({appId: '${facebook_app_id}', status: true, cookie: true,
                 xfbml: true});
	FB.Event.subscribe('auth.login', function(response) {
            $('#sign_up div.sign_up_0').hide();
    	    $('#sign_up div.sign_up_1').hide();
	    $('#sign_up div.sign_up_2').show();
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
