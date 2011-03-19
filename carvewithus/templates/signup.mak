<%inherit file="base.mak"/>

<fb:login-button>Sign Up with Facebook</fb:login-button>
% if id:
    <p><a href="${profile_url}"><img src="http://graph.facebook.com/${id}/picture?type=square"/></a></p>
% endif
<form method="post">
${fs.render()}
<input type="submit" value="save">
</form>


<div id="fb-root"></div>
<script>
    window.fbAsyncInit = function() {
        FB.init({appId: '${facebook_app_id}', status: true, cookie: true,
                 xfbml: true});
    };
    (function() {
        var e = document.createElement('script');
        e.type = 'text/javascript';
        e.src = document.location.protocol + '//connect.facebook.net/en_US/all.js';
        e.async = true;
        document.getElementById('fb-root').appendChild(e);
    }());
</script>
