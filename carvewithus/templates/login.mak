<%inherit file="base.mak"/>
<div class="container_12">
<div id="content" class="grid_6 push_3 content">
    <div class="bar fill blue">
        <h3 class="white">Log in</h3>
    </div>
    <form method="post" id="login_form" class="signup_form" name="login_form">
        <div class="clear"></div>
% if form:
	${form|n}
% endif
    </form>
</div>
