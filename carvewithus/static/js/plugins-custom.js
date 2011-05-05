
/* Sample of how to use tip */

$(document).ready(function(){
	
	/*
	$('textarea').click(function(){
		
		$('textarea').tooltip({	position:'left', 
								class: 'error', 
								content: 'something here',
								offset: {top: 0, left: 20}
								}).tooltip('show');
		return false;
	});
	*/
	
	$('input[type="text"]').promptText();
	$('textarea').promptText();
	
	$('#btn_next').click(function(){
		
		$('textarea').tooltip('destroy');
		return false;
	});
	
	/* ***************Auto Complete Invite Names*****************/
	
		function split(val) {
			return val.split(/,\s*/);
		}
		function extractLast(term) {
			return split(term).pop();
		}
		
		var cache = {},
			lastXhr;
			
		$("#txt-invite-to")
			// don't navigate away from the field on tab when selecting an item
			.bind( "keydown", function(event) {
				if (event.keyCode === $.ui.keyCode.TAB && $(this).data("autocomplete").menu.active ) {
					console.log('test');
					event.preventDefault();
				}
			})
			.autocomplete({
				source: function( request, response ) {
					
					var names = ["Adam","Ben","Phu","Ashley","Adley"];
					
					response( $.ui.autocomplete.filter(
						names, extractLast( request.term ) ) );
								
				},
				search: function() {
					// custom minLength
					var term = extractLast( this.value );
					if ( term.length < 1 ) {
						return false;
					}
				},
				focus: function() {
					// prevent value inserted on focus
					return false;
				},
				autoFocus: true,
				select: function( event, ui ) {
					var terms = split( this.value );
					// remove the current input
					terms.pop();
					// add the selected item
					terms.push( ui.item.value );
					// add placeholder to get the comma-and-space at the end
					terms.push( "" );
					this.value = terms.join( ", " );
					return false;
				}
			});
	
		/* ***********End Auto Complete Invite Names*****************/
	
	
	
});

