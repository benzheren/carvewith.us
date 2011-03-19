<%inherit file="base.mak"/>
<div class="container_12" id="sign_up">
<div class="grid_6 prefix_3 suffix_3" id="sign_up_0">
    <div class="title">
        Sign up
    </div>
    <div class="top">
        <fb:login-button size="xlarge">Connect Your Facebook Account</fb:login-button>
    </div>
    <div class="bottom">
        <a href="#" id="sign_up_with_email_link">Sign Up With Email</a>
    </div>
</div>
<div class="grid_6 prefix_3 suffix_3" id="sign_up_1" style="display:none">
    <div class="title">
        Sign up
    </div>
    <div>
	<form method="post">
            ${fs.render()}
	    <input type="submit" value="save">
        </form>
    </div>
<div>

% if id:
    <p><a href="${profile_url}"><img src="http://graph.facebook.com/${id}/picture?type=square"/></a></p>
% endif

</div>

<div id="fb-root"></div>
<script>
    window.fbAsyncInit = function() {
        FB.init({appId: '${facebook_app_id}', status: true, cookie: true,
                 xfbml: true});
	FB.Event.subscribe('auth.login', function(response) {
            console.log('create', response);
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
