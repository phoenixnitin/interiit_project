$(document).ready(function(){
	$('.controls select').addClass('btn-primary');
	$('.controls input').addClass('btn-primary');
	$('#id_sport_name_container input').prop('disabled', 'true');
  $('#id_sport_name_container').parent().remove();
});