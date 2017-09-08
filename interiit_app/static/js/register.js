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
    if($('#sel2').val() === 'participant')
        $('#gender-selector').removeClass('hide');
    else
        $('#gender-selector').addClass('hide');
    return $('#sel2').val();
}

function gender() {
    return $('#sel3').val();
}

function getRegistrationForm(){
    var host = window.location.origin;
    var sport = $('#sel1').val();
    var category = $('#sel2').val();
    var url;
    if (category === 'facultyandstaff')
    {
        switch(sport){
            case 'aquatics': url = host+'/sport/'+sport+'/facultyandstaff';break;
            default: url="";
        }
    }
    else if (category === 'participant'){
        var gender = $('#sel3').val();
        switch(sport){
            case 'aquatics': url = host+'/sport/'+sport+'/'+gender;break;
            default: url = "";
        }
    }
    else {
        url = "";
    }

    if(url !== ""){
        window.open(url, '_blank');
    }
    else
        alert("Registration form not available");
}