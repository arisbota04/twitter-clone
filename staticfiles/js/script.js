//////////////////////////
// Javascript for posts //
//////////////////////////
$(function() {
    //Executed when js-menu-icon clicled
    $('.js-menu-icon').click(function() {
        //$(this): Self element, namely div.js-menu-icon
        //next(): Next to div.js-menu-icon, namely div.menu
        //toggle: switch show and hide
        $(this).next().toggle();
    })
})