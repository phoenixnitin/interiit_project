/**
 * Created by light on 7/9/17.
 */
$(document).ready(function(){
    setTopMargin();
    $('#sel1').bind('change',function(){
        sport();
    });
    $('#sel2').bind('change',function(){
        category();
        setTopMargin();
    });
    $('#sel3').bind('change',function(){
        gender();
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
        $('.male').removeClass('hide');
        $('#sel1').val('---');
    }
    else {
      $('#sport-selector').addClass('hide');
      $('#sel1').val('---');
    }
    return $('#sel2').val();
}

function gender() {
    if($('#sel3').val() === 'men')
      $('.male').removeClass('hide');
    else
      $('.male').addClass('hide');
    $('#sel1').val('---');
    return $('#sel3').val();
}

function getRegistrationForm(){
    var host = window.location.origin;
    var sport = $('#sel1').val();
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