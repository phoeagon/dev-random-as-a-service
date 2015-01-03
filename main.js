
$(document).ready(function() {
    var refs = $('h2');
    for (var idx = 0; idx < refs.length; ++idx) {
        if (idx > 0) {
            var c = $(refs[idx-1]).prev().children();
            $(refs[idx]).append(
                $('<a>').addClass('scroll').attr('href', '#'+$(c[0]).attr('name')).text('[Prev]')
            );
        }
        if (idx != refs.length - 1) {
            var c = $(refs[idx+1]).prev().children();
            $(refs[idx]).append(
                $('<a>').addClass('scroll').attr('href', '#'+$(c[0]).attr('name')).text('[Next]')
            );
        }
        $(refs[idx]).append(
                $('<a>').addClass('scroll').attr('href', '#top').text('[Top]')
        );
        $(refs[idx]).append(
                $('<a>').addClass('scroll').attr('href', '#footer').text('[Down]')
        );
    }
    
    $('body').localScroll({duration:200});
})
