var x = 0;
$(document).ready(function(){
$(document).scroll(function() {
	//console.log('here')
	//console.log($(document.body).prop('scrollHeight'))
	var menuh = $('#top_top').prop('scrollHeight')
	console.log(menuh)
	var topheight = $('#home').prop('scrollHeight')
	var position = $(window).scrollTop()
	if (position <= (topheight - menuh) ) {
		//$('#top_top').addClass('fixed-top');
		$('#top_top').removeClass('top_m')
	}
	else if(position > (topheight - menuh)){
	$('#top_top').addClass('top_m')
	//$('#top_top').removeClass('fixed-top');
}
});
});
