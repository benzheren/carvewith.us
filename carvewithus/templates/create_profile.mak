<%inherit file="base.mak"/>

<div id="subhead">
    <div class="title">
    	<h3 class="grid_7">Create your profile</h3>
    </div>    
</div>

<div id="content" class="container_12">

<form id="create_profile_form" name="create_profile_form" method="post">
    <div class="omega grid_3 create_profile_main">
	<img src="${request.static_url('carvewithus:static/images/cat.jpg')}" class="profile_pic">
	<div class="clear"></div>
	<a class="button medium gray right" id="btn_upload" href="pic-upload">Upload Picture</a>
	<a href="" id="" class="link">Remove Picture</a>
        <input id="reg_profile_pic" name="reg_profile_pic" type="file">	
    </div>
    <div class="alpha grid_9" id="column_main">
    	
    	<div id="" class="outer">
            <label for="new_title"><h4>What Do You Do?</h4></label>
            <p>
  		<input type="radio" name="reg_activity" value="SKI"><b>Ski</b><br>
		<input type="radio" name="reg_activity" value="SNOWBOARD"><b>Snowboard</b><br>
		<input type="radio" name="reg_activity" value="BOTH"><b>Both</b><br>
  	    </p>
       	</div>

        <div id="" class="outer">
            <label for="new_summary"><h4>Skill Level</h4></label>
            <p>
  		<input type="radio" name="reg_level" value="NEWBIE"><b>Newbie</b><br>
		<input type="radio" name="reg_level" value="INTERMEDIATE"><b>Intermediate</b><br>
		<input type="radio" name="reg_level" value="ADVANCED"><b>Advanced</b><br>
		<input type="radio" name="reg_level" value="EXPERT"><b>Expert</b><br>
            </p>
       	</div>
    </div>

</form>

<div class="bar line bottom">
    <div class="omega grid_3">&nbsp;</div>
    <div class="alpha grid_9">
        <a href="#" id="create_profile_done" class="button huge blue">Done</a>
    </div>
</div>
<div class="clear"></div>

</div>
