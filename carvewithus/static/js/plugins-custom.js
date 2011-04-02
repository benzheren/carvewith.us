
/* Sample of how to use tip */

$(document).ready(function(){
	
	
	$('textarea').click(function(){
		
		$('textarea').tooltip({	position:'left', 
								class: 'error', 
								content: 'something here',
								offset: {top: 0, left: 20}
								}).tooltip('show');
		return false;
	});
	
	$('#btn_next').click(function(){
		
		$('textarea').tooltip('destroy');
		return false;
	});
});

