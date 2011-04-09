<%inherit file="base.mak"/>
<!----- SubHead Start ----->
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
<!----- SubHead End ----->


<!----- Content Start ----->

<div id="content" class="content container_12">
<div class="bar line top">
	<h3 class="dark">Basic Details</h3>
	<a class="button medium gray right" id="btn_view" href="viewtrip">View Trip Profile</a>
</div>
% if form:
	${form|n}
% endif
</div>
