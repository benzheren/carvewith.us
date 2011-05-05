/****************************
*	jQuery textPrompt 
*	by various, compilated by Phu
*	Displays 'prompt' text inside an form text input element
*	'prompt' text will disappear when 
*	target element must be input
*	
*****************************/


(function($){

  $.fn.promptText = function() {   
    return this.each(function() {
		
		var $this = $(this);
		
		//if ($this.attr("type") != "text") return;
 
                var fontColor = $this.css("color");
                var backgroundColor = $this.css("background-color");
 				var promptText = $this.attr("alt");
				var promptColor = "#999";
				
                $this.focus(function () {
                    if (jQuery.trim($this.val()) == promptText) {
                        $this.css({ color: fontColor}).val("");
                    }
                }).blur(function () {
                    if (jQuery.trim($this.val()) == "") {
                        $this.css({ color: promptColor}).val(promptText);
                    }
                });
				
				var value = $this.val();
                if (value == "" || value == promptText) {
                    $this.css({color: promptColor}).val(promptText);
                }
	});
  };

})(jQuery);




