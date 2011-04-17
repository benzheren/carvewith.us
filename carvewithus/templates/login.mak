<%inherit file="base.mak"/>
<%!
from webhelpers.html.tags import text, password, checkbox, hidden
%>
<div class="container_12">
<div id="content" class="grid_6 push_3 content">
    <div class="bar fill blue">
        <h3 class="white">Log in</h3>
    </div>
    <form method="post" id="login_form" class="signup_form" name="login_form">
	    % if 'form' in errors:		    
	    <div class="bar msg error" style="">
        	<div class="msgicon"></div>
		<h4 class="white">Don't have an account? Click <a href="/signup">here</a> to register</h4>
	     </div>
            % else:
		<div class="clear"></div>
     	    % endif
	    <table class="verticalform" celspacing="0" cellpadding="0">
		    <tbody>
			    <tr>
				    <td class="label">
					    <label for="email">Email:</label>
				    </td>
				    <td class="input">
					    ${text(name="email", class_="text inputtext")}
				    </td>
				    <td class="error">
					    % if 'email' in errors:
					    <div class="inlinemsg error">
					    	<div class="tip"></div>
						<p class="msgtext">Email can not be empty</p>
				            </div>
					    % endif
				    </td>
			    </tr>
			    <tr>
				    <td class="label">
					    <label for="password">Password:</label>
				    </td>
				    <td class="input">
					    ${password(name="password", class_="text inputtext")}
				    </td>
				    <td>
					    % if 'password' in errors:
					    <div class="inlinemsg error">
					    	<div class="tip"></div>
						<p class="msgtext">Password can not be empty</p>
				            </div>
					    % endif

				    </td>
			    </tr>
			    <tr>
				    <td class="label"></td>
				    <td>
					    ${checkbox(name="remember_me", value="1", checked=True)}
					    <label for="remember_me">Remeber me on this computer</label>
				    </td>
				    <td></td>
			    </tr>
			    <tr>
				    <td class="label"></td>
				    <td class="description">
					    <a class="button large red" href="#" id="login_btn">Log in</a>
				    </td>
				    <td></td>
			    </tr>
		    </tbody>
	    </table>
	    ${hidden(name="_csrf_", value=_csrf_)}
    </form>
</div>
