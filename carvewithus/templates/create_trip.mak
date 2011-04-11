<%inherit file="base.mak"/>
<%! 
from webhelpers.html.tags import form, end_form, text, textarea, radio, checkbox
%>
<div class="subhead_container">
    <div class="subhead">
        <div class="title">
            <h3 class="grid_7">Organize a new trip</h3>
        <ul class="submenu  grid_5">
            <li class="active"><a href="basic"><b>1.</b> Basic Details</a>
            <div class="tip"></div>
            </li>
            <li><a href="logistics"><b>2.</b> Logistics</a></li>
            <li><a href="members"><b>3.</b> Members</a></li>
        </ul>
        </div>
    </div>
</div>

<div id="content" class="content container_12">
${form('/submit',method='post')}
<div class="bar line top">
	<h3 class="dark">Basic Details</h3>
	<a class="button medium gray right" id="btn_view" href="viewtrip">View Trip Profile</a>
</div>
<div class="column_1 grid_3">
	<img src="" class="trip_pic" />
    	<div class="clear"> </div>
        <a href="pic-upload" id="btn_upload" class="button medium gray right">Upload Picture</a>
	<a href="pic-clear" id="btn_remove" class="link">Remove Picture</a>
        <div class="clear"> </div>
</div>
<div id="column_main_basic" class="grid_9 column_main">
    	<div id="title" class="outer">
        	<label for="new_title"><h4>Title</h4></label>
		<p id="description">
			${text(name='new_title', class_='text large full', alt_='Enter trip title (50) chars')}
  		</p>
       	</div>
        <div id="summary" class="outer">
        	<label for="new_summary"><h4>Trip Summary</h4></label>
		<p id="description">
			${textarea(name='new_summary', class_='text small full')}
            	</p>
       	</div>
</div>
<div class="bar line bottom">
	<div class="column_1 grid_3"></div>
	<div class="grid_4">
            <a href="next-logistics" id="btn_next" class="button huge blue">Next  &rarr;</a>
        </div>
</div>
${end_form()}
</div>
<div id="content" class="content container_12">
	<div class="bar line top">
        	<h3 class="dark">Logistics</h3>
            	<a href="viewtrip" id="btn_view" class="button medium gray right">View Trip Profile</a>
        </div>
	<div id="column_main_logistics" class="grid_8 column_main">
    		<div class="clear"></div>
		${form('/submit', method='post', name='new_trip_logistics')}
	    	<div id="itinerary" class="outer">
			<h4>Intinerary</h4>
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
                        	<tbody>
                        	<tr>
		        		<td class="number">
		            			<label class="lblleft">1</label>
		            		</td>
					<td class="location">
						${text(name='new_loc_1', class_='text medium arrdest', alt_='Enter City Name')}
					</td>
					<td class="date">
						${text(name='new_date_1', type='date', class_='text medium arrdest', alt_='Enter Date')}
					</td>
					<td class="time">
						<select id="txt_new_time_1" name="new_time_1" class="text medium arrdest" alt="Enter Time">
							<option value="">Enter Time</option>
						</select>
					</td>
		            	</tr>
                        	<tr>
		            		<td class="number">
		            			<label class="lblleft">2</label>
		            		</td>
					<td class="location">
								<input id="txt_new_loc_2" name="new_loc_2" class="text medium arrdest" alt="Enter City Name" />
							</td>
							<td class="date">
								<input id="txt_new_date_2" name="new_date_2" class="text medium arrdest" alt="Enter Date" />
							</td>
							<td class="time">
								<select id="txt_new_time_2" name="new_time_2" class="text medium arrdest" alt="Enter Time">
									<option value="">Enter Time</option>
								</select>
							</td>
		            	</tr>
                        	</tbody>
                        	<tfoot>
                        	<tr>
                        		<td class="number"></td>
                            		<td class="location">
                            			<a href="next-logistics" id="btn_next" class="button medium gray">Add Destination +</a>
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
						<label class="lbltop">Method</label>
					</td>
					<td class="date">
						<label class="lbltop">Spots Available</label>
					</td>
				</tr>
                        	</thead>
                        	<tbody>
                        	<tr>
		            		<td class="number">
		            			<img class="col_lead_icon" src="../images/trip_icon_car.png" />
		            		</td>
					<td class="location">
						${radio(name='transport_method', value='Driving')}
						${radio(name='transport_method', value='Public')}
					</td>
					<td class="date">
						${text(name='spots', type='number', class_='text small arrdest', alt_='Enter Spots')}
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
						<label class="lbltop">Have Lodging?</label>
					</td>
					<td class="date" colspan="2">
						<label class="lbltop">Lodging Description</label>
					</td>
		            	</tr>
                        	</thead>
                        	<tbody>
                        	<tr>
		            		<td class="number">
		            			<img class="col_lead_icon" src="../images/trip_icon_house.png" />
		            		</td>
					<td class="location">
						${checkbox(name='have_lodging', value='1')}
                                		<label for="have_lodging">Yes</label>
					</td>
					<td class="lodge" colspan="2">
						${text(name='lodging_desc', class_='text medium arrdest', alt_='Enter Lodging Details')}
					</td>		
		            	</tr>
                       		</tbody>
                     		</table>
			</p>
	       	</div>
		${end_form()}			
	</div>
        <div class="bar line bottom">
        	<div class="grid_3">
        		<a href="next-logistics" id="btn_next" class="button large gray right">&larr; Back</a>
        	</div>
        	<div class="grid_4">
            		<a href="next-logistics" id="btn_next" class="button huge blue">Next  &rarr;</a>
            	</div>
        </div>
 	<div class="clear"> </div>
</div>

