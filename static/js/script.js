$(document).ready(function(){
    $('.sidenav').sidenav();
    $('.parallax').parallax();
    $('.tabs').tabs();
    $('select').formSelect();
    $('.tooltipped').tooltip();
    $('.collapsible').collapsible();
    
    $('#textarea1').val('');
    M.textareaAutoResize($('#textarea1'));
    
});

document.getElementById("questions").addEventListener("keyup", getDataFn);

function getDataFn() {
    questionsPerRound = parseInt(document.getElementById('questions').value);

    questionsVSdifficultyFN(questionsPerRound);
};

function questionsVSdifficultyFN(questionsPerRound){
    document.getElementById('easy').value = questionsPerRound;
};