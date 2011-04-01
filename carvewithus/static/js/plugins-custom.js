/* for jQuery qTip */
$.fn.qtip.styles.inlineerror = { // Last part is the name of the style
   width: 200,
   textAlign: 'left',
   tip: { corner: 'leftMiddle'},
   border: { color: '#CC0000' },
   'font-size': '1.2em',
   'font-weight': '900',
   'padding':'10px',
   'box-shadow': '1px 1px 5px rgba(0,0,0,0.5)',
   '-moz-box-shadow': '1px 1px 5px rgba(0,0,0,0.5)',
   '-webkit-box-shadow': '1px 1px 5px rgba(0,0,0,0.5)',
   color:'#FFF',
   background:'#CC0000'
   
};

/* Sample of how to use qTip */

$(document).ready(function(){
	
	$('input').qtip({
		content: 'This could be html as well',
	   	show: 'focus',
   		hide: 'blur',
		style: 'inlineerror',
		position: { corner: { target: 'rightMiddle', tooltip:'leftMiddle'} }
		
	});
	
	$('textarea').click(function(){
		$('textarea').qtip({
			content: 'this tooltip is initiated one time only',
			show: false,
			hide: false,
			style: 'inlineerror',
			position: { corner: { target: 'rightMiddle', tooltip:'leftMiddle'} }
		
		})
		$('textarea').qtip("show",{content: 'dude'});
	});
});





