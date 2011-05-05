<%inherit file="base.mak"/>
<%! 
from webhelpers.html.tags import text, textarea, radio, checkbox
%>
<div class="subhead_container">
    <div class="subhead">
        <div class="title">
            <h3 class="grid_7">Organize a new trip</h3>
        <ul class="submenu  grid_5">
		<li id="create_trip_menu_1" class="active"><a href="#" alt="1"><b>1.</b> Basic Details</a>
            </li>
	    <li id="create_trip_menu_2"><a href="#" alt="2"><b>2.</b> Logistics</a></li>
	    <li id="create_trip_menu_3"><a href="#" alt="3"><b>3.</b> Members</a></li>
        </ul>
        </div>
    </div>
</div>
<div id="create_trip_1" class="content container_12 create_trip_form">
<div class="bar line top">
	<h3 class="dark">Basic Details</h3>
	<a class="button medium gray right" id="btn_view" href="viewtrip">View Trip Profile</a>
</div>
<div class="column_1 grid_3">
	<form method="post" action="/upload" enctype="multipart/form-data" id="create_trip_pic_form" class="pic_upload">
		<img src="" class="trip_pic" />
		<div class="clear"> </div>
		<a class="button medium gray" href="#" id="upload_widget_btn">Upload Picture</a>
		<a href="" id="" class="link">Remove Picture</a>
		<input name="picture.upload" type="file" class="upload_widget" size="15" style="display:none;">
		<input name="picture.static" type="hidden">
		<input type="submit" value="Upload" class="upload_widget" style="display:none;">
		<input type="submit" value="Cancel" class="upload_widget" style="display:none;" id="upload_widget_cancel">
		<input type="hidden" name="pic_form" value="create_trip_pic_form">
		<input type="hidden" name="target_form" value="create_profile_basic_form">
		${form.csrf_token()}
	</form>
        <div class="clear"> </div>
</div>
<div id="column_main_basic" class="grid_9 column_main">
	${form.begin(url=request.route_url('create_trip_post'), id_="create_trip_basic_form")}
	${form.hidden(name='picture')}
	<div id="title" class="outer">
		<h4>${form.label('name', label='Title')}</h4>
		<p>
			${form.text(name='name', class_='text large full', alt_='Enter trip title (50) chars')}
  		</p>
       	</div>
	<div id="summary" class="outer">
		<h4>${form.label(name='summary', label='Trip Summary')}</h4>
		<p>
			${form.textarea(name='summary', class_='text small full')}
            	</p>
	</div>
	${form.csrf_token()}
	${form.end()}
</div>
<div class="bar line bottom">
	<div class="column_1 grid_3"></div>
	<div class="grid_4">
		<a href="#" alt="2" class="button huge blue btn_next">Next  &rarr;</a>
        </div>
</div>
</div>
<div id="create_trip_2" class="content container_12 create_trip_form" style="display: none;">
	<div class="bar line top">
        	<h3 class="dark">Logistics</h3>
            	<a href="viewtrip" id="btn_view" class="button medium gray right">View Trip Profile</a>
        </div>
	<div id="column_main_logistics" class="grid_8 column_main">
	${form.begin(url=request.route_url('create_trip_post'), id_="create_trip_basic_form")}
    		<div class="clear"></div>
	    	<div id="itinerary" class="outer">
			<h4>Intinerary</h4>
			${form.hidden(name='itinerary_count', value='2')}
			<p id="description">
				<table cellpadding="0" cellspacing="0" class="itinerary_edit grid_9">
		            	<thead>
		            	<tr>
                        		<td class="number"></td>
					<td class="location">
						<label class="lbltop">Starting Location</label>
					</td>
					<td class="date">
						<label class="lbltop">Date</label>
					</td>
					<td class="time">
						<label	s class="lbltop">Time</label>
					</td>
		        	</tr>
                        	</thead>
				<tbody id='itinerary-table'>
				<tr id='itineraries-0'>
		        		<td class="number">
		            			<label class="lblleft">1</label>
		            		</td>
					<td class="location">
						${form.text(name='itineraries-0.location', class_='text medium arrdest', alt_='Enter City Name')}
					</td>
					<td class="date">
						${form.text(name='itineraries-0.date', type='date', class_='text medium arrdest', alt_='Enter Date')}
					</td>
					<td class="time">
						${form.select(name='itineraries-0.time', options=[('', 'Enter Time') ], class_='text, medium, arrdest', alt_='Enter Time')}
					</td>
		            	</tr>
                        	<tr>
		            		<td class="number">
		            			<label class="lblleft">2</label>
		            		</td>
					<td class="location">
						${form.text(name='itineraries-1.location', class_='text medium arrdest', alt_='Enter City Name')}
					</td>
					<td class="date">
						${form.text(name='itineraries-1.date', type='date', class_='text medium arrdest', alt_='Enter Date')}
					</td>
					<td class="time">
						${form.select(name='itineraries-1.time', options=[('', 'Enter Time') ], class_='text, medium, arrdest', alt_='Enter Time')}
					</td>
	
		            	</tr>
                        	</tbody>
                        	<tfoot>
                        	<tr>
                        		<td class="number"></td>
                            		<td class="location">
						<a href="#" id="add_dest_btn" class="button medium gray">Add Destination +</a>
                            		</td>
                            		<td>
                            			<input id="chk_round_trip" name="round_trip" type="checkbox" value="roundtrip" />
                                		<label for="round_trip">Round Trip</label>
                            		</td>
                        	</tr>
                        	</tfoot>
		  		</table> 
	  		</p>
	       	</div>
            
		<div class="separator"></div>
		<div class="clear"></div>
            
	        <div id="transportation" class="outer">
	        	<h4>Transportation</h4>
	            	<p id="description">
	  			<table cellpadding="0" cellspacing="0" class="itinerary_edit grid_9">
		            	<thead>
		            	<tr>
                        		<td class="number"></td>
					<td class="location">
						${form.label(name='transportation', class_='lbltop', label='Method')}
					</td>
					<td class="date">
						${form.label(name='spots_available', class_='lbltop', label='Spots Available')}
					</td>
				</tr>
                        	</thead>
                        	<tbody>
                        	<tr>
					<td class="number">
						<div class="icon48 car"></div>
		            		</td>
					<td class="location">
						${form.radio(name='transportation', value='DRIVE', label='Driving')}
						<br/>
						${form.radio(name='transportation', value='BUS', label="Public/Bus")}
					</td>
					<td class="date">
						${form.text(name='spots_available', type='number', class_='text small arrdest', alt_='Enter Spots')}
					</td>
					<td class="time"></td>
		            	</tr>
                       		</tbody>
                     		</table>
			</p>
	       	</div>
	        <div id="lodging" class="outer">
	        	<h4>Lodging</h4>
	            	<p id="description">
	  			<table cellpadding="0" cellspacing="0" class="itinerary_edit grid_9">
		            	<thead>
		            	<tr>
                        		<td class="number"></td>
					<td class="location">
						${form.label(name='has_lodge', label='Have Lodging', class_='lbltop')}
					</td>
					<td class="date" colspan="2">
						${form.label(name='lodge_desc', label='Lodging Description', class_='lbltop')}
					</td>
		            	</tr>
                        	</thead>
                        	<tbody>
                        	<tr>
		            		<td class="number">
		            			<img class="col_lead_icon" src="../images/trip_icon_house.png" />
		            		</td>
					<td class="location">
						${form.checkbox(name='has_lodge', value='1')}
						<label for="has_lodge">Yes</label>
					</td>
					<td class="lodge" colspan="2">
						${form.text(name='lodge_desc', class_='text medium arrdest', alt_='Enter Lodging Details')}
					</td>		
		            	</tr>
                       		</tbody>
                     		</table>
			</p>
		</div>
	${form.csrf_token()}
	${form.end()}
	</div>
        <div class="bar line bottom">
        	<div class="grid_3">
			<a alt="1" href="#" class="button large gray right btn_next">&larr; Back</a>
        	</div>
        	<div class="grid_4">
			<a alt="3" href="#" class="button huge blue btn_next">Next  &rarr;</a>
            	</div>
        </div>
 	<div class="clear"> </div>
</div>
<div id="create_trip_3" class="content container_12 create_trip_form" style="display: none;">

	<!----- Top bar ----->
        <div class="bar line top">
        	<h3 class="dark">Invite your friends!</h3>
            <a href="viewtrip" id="btn_view" class="button medium gray right">View Trip Profile</a>
        </div>
   <!----- end Top bar ----->
   
   
   <!----- Top bar ----->
        <div class="bar line members">
        	<div class="grid_4">
            	&nbsp;
            </div>
            <ul class="tab">
                <li class="active">
                	<a href="">Invite</a>
                    <sup>2</sup>
                </li>
            </ul>
        </div>
   <!----- end Top bar ----->
   
	
    <!----- Right Column / Invite Message----->
	<div id="column_left_contact" class="grid_4 column_1">
       	<div class="outer">
       		<fb:login-button size="large">Connect Your Facebook Account</fb:login-button>
        </div>
        <div class="outer">
        	<label class="top">Add by name or email</label>
            <input id="txt_" type="text" class="text large searchname" alt="Type in friend's name or email" />
            <a href="invite" id="btn_invite" class="button medium green right">Add &raquo;</a>
        </div>
        <div class="outer">
        	<label class="top">List of Facebook friends</label>
            <ul class="users_list full friends">
            <li>
                <h6 class="name">User Name</h6>
                <a href="addinvite" class="button medium green right msg">&raquo;</a>
            </li>
             <li class="alt">
                <h6 class="name">User Name</h6>
                <a href="addinvite" class="button medium green right msg">&raquo;</a>
            </li>
            </ul>
        </div>
        
    </div>
    <!----- End Right Column Invite Message ----->
    
	 <!----- Main Column / People ----->
	<div id="column_main_people" class="grid_8 column_main">
        
        <div class="outer">
        	<h4 class="tabhead">Invite List:</h4>
        	<ul class="users_list full">
            <li>
                <div class="grid_1">
                	<img class="small" src="" />
                </div>
                <div class="grid_5">
                    <h6 class="name">User Name</h6>
                    <div class="skill">
                        <span class="activity">Snowboard</span>
                        <span class="activity">Ski</span>
                    </div>
                    <p class="info">
                        If the person is not on CWS but on facebook, this is blank.
                    </p>
                </div>
                
                <a href="uninvite" class="button medium red right msg">X</a>
            </li>
            <li class="alt">
                <div class="grid_1">
                	<img class="small" src="" />
                </div>
                <div class="grid_5">
                    <h6 class="name">just-an-email-address@something.com</h6>
                   
                </div>
                
                <a href="uninvite" class="button medium red right msg">X</a>
            </li>
            
            </ul>
        </div>
        
    </div>
    <!----- End Main Column People ----->
    
	

   

    <!----- Bottom bar ----->
        <div class="bar line bottom">
		<div class="grid_3">
			<a alt="2" href="#" class="button large gray right btn_next">&larr; Back</a>
        	</div>
        	<div class="grid_4">
			<a href="#" id="create_trip_btn" class="button huge blue">Done!</a>
            </div>
        </div>
   <!----- end Bottom bar ----->

 <div class="clear"> </div>
</div>
