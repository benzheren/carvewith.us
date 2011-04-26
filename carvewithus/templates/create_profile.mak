<%inherit file="base.mak"/>
<div class="subhead_container">
	<div class="subhead">
    <div class="title">
    	<h3 class="grid_7">Create your profile</h3>
    </div>    
</div>
</div>

<div class="content container_12">
	<div class="bar line top">
		<h3 class="dark">Basic Information</h3>
	</div>
	<div class="column_1 grid_3 create_profile_main">
		<form method="post" action="/upload" enctype="multipart/form-data" id="create_profile_pic_form">
			<img src="${request.static_url('carvewithus:static/images/cat.jpg')}" class="profile_pic">
			<div class="clear"></div>
			<a class="button medium gray" id="btn_upload" href="pic-upload">Upload Picture</a>
			<a href="" id="" class="link">Remove Picture</a>
			<input name="picture.upload" type="file">
			<input name="picture.static" type="hidden">
			<input type="submit" value="Upload">
			<input type="hidden" name="pic_form" value="create_profile_pic_form">
			<input type="hidden" name="target_form" value="create_profile_form">
			${form.csrf_token()}
		</form>
	</div>
	<div class="grid_9 column_main">

	${form.begin(url=request.route_url('create_profile'), id_="create_profile_form")}
	${form.hidden(name='picture')}
    	<div id="" class="outer">
            <label for="new_title"><h4>What Do You Do?</h4></label>
	    <p>
		    ${form.radio(name="activity", value="SNOWBOARD", label="Snowboard")}
		    <br/>
		    ${form.radio(name="activity", value="SKI", label="Ski")}
	    	    <br/>
		    ${form.radio(name="activity", value="BOTH", label="Both")}	    
  	    </p>
       	</div>

        <div id="" class="outer">
            <label for="new_summary"><h4>Skill Level</h4></label>
	    <p>
		    ${form.radio(name="skill_level", value="NEWBIE", label="Newbie")}
		    <br/>
		    ${form.radio(name="skill_level", value="INTERMEDIATE", label="Intermediate")}
		    <br/>
		    ${form.radio(name="skill_level", value="ADVANCED", label="Advanced")}
		    <br/>
		    ${form.radio(name="skill_level", value="EXPERT", label="Expert")}
            </p>
       	</div>
	</div>
	${form.csrf_token()}
	${form.end()}
	<div class="bar line bottom">
		<div class="column_1 grid_3">&nbsp;</div>
		<div class="grid_4">
			<a href="#" id="create_profile_done" class="button huge blue">Done</a>
	    	</div>
	</div>
	<div class="clear"></div>
</div>


