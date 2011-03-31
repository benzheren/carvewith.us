<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta http-equiv="Content-Type" content="text/html;charset=UTF-8"/>
    <link rel="stylesheet" href="${request.static_url('carvewithus:static/css/960reset.css')}" 
    type="text/css" media="screen" charset="utf-8"/>
    <link rel="stylesheet" href="${request.static_url('carvewithus:static/css/main.css')}" 
    type="text/css" media="screen" charset="utf-8"/>
    <script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.5.1/jquery.min.js"></script>
    <script type="text/javascript" src="${request.static_url('carvewithus:static/js/jquery.form.js')}"></script>
    <script type="text/javascript" src="${request.static_url('carvewithus:static/js/main.js')}"></script>

</head>
<body>
<div id="banner">
    <div id="head">
        <div class="logo"><h1>carvewith.us</h1></div>
        
        <ul class="menu">
            <li><a href="/trip/join">
                <h2>Join Trip</h2>
                <span class="sub">Find a trip to join</span>
            </a></li>
            <li><a href="/trip/create">
                <h2>Organize</h2>
                <span class="sub">Make a new trip</span>
            </a></li>
        </ul>
        
        <div id="account">
% if not user_email:
            <div id="login_links">
                <a href="/login">login</a>&nbsp;|&nbsp;<a href="signup">sign up</a>
            </div>
% else:
            <div id="account_links">
                <span>Hi, ${user_email}</span>
                &nbsp;|&nbsp;
                <a href="account">my account</a>
                &nbsp;|&nbsp;
                <a href="/logout">logout</a>
            </div>
% endif
        </div>
    </div>
</div>

${self.body()}

</body>
</html>
