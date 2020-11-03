$(document).ready(function(){
    $('.sidenav').sidenav();
    $('.tabs').tabs();
    $('select').formSelect();
    $('.tooltipped').tooltip();
    $('#textarea1').val('');
    M.textareaAutoResize($('#textarea1'));
});

