function cross_section_link(){
    var refs = $('h2');
    for (var idx = 0; idx < refs.length; ++idx) {
        if (idx > 0) {
            var c = $(refs[idx-1]).prev().children();
            $(refs[idx]).append(
                $('<a>').addClass('scroll btn btn-xs btn-success')
                .attr('href', '#'+$(c[0]).attr('name')).text('Prev')
            );
        }
        if (idx != refs.length - 1) {
            var c = $(refs[idx+1]).prev().children();
            $(refs[idx]).append(
                $('<a>').addClass('scroll btn btn-xs btn-warning')
                .attr('href', '#'+$(c[0]).attr('name')).text('Next')
            );
        }
        $(refs[idx]).append(
                $('<a>').addClass('scroll btn btn-xs btn-info')
                .attr('href', '#top').text('Top')
        );
        $(refs[idx]).append(
                $('<a>').addClass('scroll btn btn-xs btn-info')
                .attr('href', '#footer').text('Down')
        );
    }
}
$(document).ready(function() {
    
    $('body').localScroll({duration:200});
    var accordion_cont = $('#accordion_pre').parent().nextUntil('#accordion_post');
    $(accordion_cont).remove();
    $('#accordion_post').append($(accordion_cont));
    var e = ['a[name=home]', 'a[name=features]', 'a[name=pricing]',
    'a[name=api]', 'a[name=contact]',  'a[name=epilog]'];
    for (var i = 0 ; i < e.length-1; ++i){
        var eles = $(e[i]).parent().next().nextUntil($(e[i+1]).parent());
        console.log(eles);
        $(eles).remove();
        $(e[i]).parent().next().after($('<div>').append($(eles)));
    }
    $('#accordion_post').accordion({
        'header': 'h2',
        'heightStyle': 'content',
    });
    //cross_section_link();
})
