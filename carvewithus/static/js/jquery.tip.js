(function($){

  var methods = {
     init : function(settings) {

       return this.each(function(){
         
		 var $this = $(this);
		 
		 if(!($this.data('tip'))) {
			$html = '<div class="inlinemsg '+settings.class+'"><div class="tip"></div><p class="msgtext">'+settings.content+'</p></div>';
			$this.parent().append($html);
			$this.data('tip',settings);
		 } 
       });
     },
   
     reposition : function( ) { // TO add reposition script in case of window resize
	 },
     show : function() { 
	 	
		return this.each(function(){
			var $this = $(this);
			$tooltip = $this.next('.inlinemsg');
			$tooltip = $this.next('.inlinemsg');
			$tooltip.offset(
			{ 	top: $this.offset().top,
				left: $this.offset().left+$this.width()+$this.data('tip').offset.left
			});
			$tooltip.show();
			
		})
	 },
     destroy : function( ) { 
	 	return this.each(function(){
			var $this = $(this);
			$this.removeData('tip');
	 		$this.next('.inlinemsg').remove();
		});
	 }
  };

  $.fn.tooltip = function( method ) {   
    if ( methods[method] ) {
      return methods[method].apply( this, Array.prototype.slice.call( arguments, 1 ));
    } else if ( typeof method === 'object' || ! method ) {
      return methods.init.apply( this, arguments );
    } else {
      $.error( 'Method ' +  method + ' does not exist on jQuery.tooltip' );
    }    
  };

})(jQuery);




