$(document).ready(function(){
	$('.controls select').addClass('btn-primary');
	$('.controls input').addClass('btn-primary');
	$('#div_id_sport_name .controls input').prop('disabled', 'true');
  $('#div_id_sport_name').remove();
});