<%inherit file="base.mak"/>
<div class="container_12">
<div id="content" class="grid_6 push_3 content">
    <div class="bar fill blue">
        <h3 class="white">Sign Up</h3>
    </div>
    <div class="sign_up_top sign_up_0">
        <fb:login-button size="xlarge">Connect Your Facebook Account</fb:login-button>
    </div>
    <div class="sign_up_1" style="display:none;">
	${form.begin(url=request.route_url('signup_post'), class_="signup_form", id_="signup_form_email")}
	    <div class="clear"></div>
	    <table class="verticalform" callpadding="0" cellspacing="0">
	        <tbody>
			<tr>
				<td class="label">${form.label('name', label='Full Name:')}</td>	
				<td class="input">${form.text('name', class_='inputtext')}</td>
			</tr>
			<tr>
				<td class="label">${form.label('email', label='Email:')}</td>
				<td class="input">${form.text('email', class_='inputtext')}</td>
			</tr>
			<tr>
				<td class="label">${form.label('password', label='Password:')}</td>
				<td class="input">${form.password('password', class_='inputtext')}</td>
			</tr>
			<tr>
				<td class="label">${form.label('city', label='City:')}</td>
				<td class="input">
					${form.select('city', options=[('sfo', 'San Francisco, CA'), 
					('nyc', 'New York City, NY'), ('chi', 'Chicago, IL'),
					('den', 'Denver, CO'), ('other', 'Other')], class_='inputtext')}
				</td>
			</tr>
			<tr>
				<td class="label"></td>
				<td>
					<input type="checkbox" value="1" name="remember_me" id="remember_me" checked="checked">									      <label for="remember_me">Remeber me on this computer</label>
				</td>
			</tr>
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
		${form.csrf_token()}
	${form.end()}
    </div>
    <div class="sign_up_2 sign_up_top" style="display:none;">
	${form.begin(url=request.route_url('signup_post'), class_="signup_form", id_="signup_form_fb")}
	    <div class="clear"></div>
	    <table class="verticalform" callpadding="0" cellspacing="0">
		   <tbody>
			<tr>
				<td class="label">${form.label('name', label='Full Name:')}</td>	
				<td class="input">${form.text('name', class_='inputtext')}</td>
			</tr>
			<tr>
				<td class="label">${form.label('email', label='Email:')}</td>
				<td class="input">${form.text('email', class_='inputtext')}</td>
			</tr>
			<tr>
				<td class="label">${form.label('password', label='Password:')}</td>
				<td class="input">${form.password('password', class_='inputtext')}</td>
			</tr>
			<tr>
				<td class="label">${form.label('city', label='City:')}</td>
				<td class="input">
					${form.select('city', options=[('sfo', 'San Francisco, CA'), 
					('nyc', 'New York City, NY'), ('chi', 'Chicago, IL'),
					('den', 'Denver, CO'), ('other', 'Other')], class_='inputtext')}
				</td>
			</tr>
			<tr>
				<td class="label"></td>
				<td>
					<input type="checkbox" value="1" name="remember_me" id="remember_me" checked="checked">									      <label for="remember_me">Remeber me on this computer</label>
				</td>
			</tr>
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
		${form.csrf_token()}
	${form.end()}
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
		    content = '<p><img src=\"http://graph.facebook.com/' + response.id +
			    '/picture?type=large\"></p>';
	        $('#fb_preview').html(content);
		$('#signup_form_fb #name').val(response.name);
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
