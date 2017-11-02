/**
 * Created by light on 7/9/17.
 */
$(document).ready(function(){
    setTopMargin();
    $('#sel1').bind('change',function(){
        sport();
        // console.log('sport changed');
    });
    $('#sel2').bind('change',function(){
        category();
        setTopMargin();
        // console.log('category changed');
    });
    $('#sel3').bind('change',function(){
        gender();
        // console.log('gender changed');
    });
    $('.container select').addClass('btn-primary');
    $(window).resize(function () {
        setTopMargin();
    });
});

function setTopMargin() {
    var winHeight = $(window).height();
    var containerHeight = $('.container').height();
    $('.container').css('margin-top', (winHeight-containerHeight)/2);
}

function sport() {
    return $('#sel1').val();
}

function category() {
    if($('#sel2').val() === 'participant'){
        $('#gender-selector').removeClass('hide');
        gender();
        $('#sport-selector').removeClass('hide');
    }
    else if ($('#sel2').val() === 'facultyandstaff'){
        $('#gender-selector').addClass('hide');
        $('#sport-selector').removeClass('hide');
        $('#sport-selector-women').addClass('hide');
        // $('.male').removeClass('hide');
        // $('#sel1').val('---');
        resetSport();
    }
    else {
      $('#sport-selector').addClass('hide');
      $('#gender-selector').addClass('hide');
      // $('#sel1').val('---');
      resetSport();
    }
    return $('#sel2').val();
}

function gender() {
    if($('#sel3').val() === 'men'){
      // $('.male').removeClass('hide');
      $('#sport-selector-women').addClass('hide');
      $('#sport-selector').removeClass('hide');
      // hideFemaleSport('men');
    }
    else{
      // $('.male').addClass('hide');
      $('#sport-selector').addClass('hide');
      $('#sport-selector-women').removeClass('hide');
      // hideFemaleSport('women');
    }
    // $('#sel1').val('---');
    resetSport();
    return $('#sel3').val();
}
function resetSport() {
  $('#sport-selector input').val('---');
  $('#sport-selector select').val("None");
  $('#sport-selector select').material_select();
  $('#sport-selector-women input').val('---');
  $('#sport-selector-women select').val("None");
  $('#sport-selector-women select').material_select();
}

function getRegistrationForm(){
    var host = window.location.origin;
    if($('#sel3').val() === 'men')
      var sport = $('#sel1').val();
    else
      var sport = $('#sel4').val();
    var category = $('#sel2').val();
    var url;
    if (category === 'facultyandstaff')
    {
        if(sport==='athletics' || sport==='badminton' || sport==='basketball' || sport==='cricket' || sport==='football' || sport==='hockey' || sport==='squash' || sport==='table_tennis' || sport==='tennis' || sport==='volleyball' || sport==='weightlifting'){
          url = host+'/sport/'+sport+'/facultyandstaff';
        }
        else
          url="";
    }
    else if (category === 'participant'){
        var gender = $('#sel3').val();
        if(sport==='athletics' || sport==='badminton' || sport==='basketball' || sport==='cricket' || sport==='football' || sport==='hockey' || sport==='squash' || sport==='table_tennis' || sport==='tennis' || sport==='volleyball' || sport==='weightlifting') {
          url = host + '/sport/' + sport + '/' + gender;
        }
        else
          url = "";
    }
    else {
        url = "";
    }
    // console.log(url);
    if(url !== ""){
        window.open(url, '_blank');
    }
    else
        alert("Registration form not available");
}