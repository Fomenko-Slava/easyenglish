app.plugins = (function ($) {

    function init() {
        navbar_menu();


    }
    
    function navbar_menu() {
        $('[data-toggle="slide-collapse"]').on('click', function() {
            $navMenuCont = $($(this).data('target'));
            $navMenuCont.css('z-index', 1000).animate({'left':'0'}, 200);
            $('#overlay_bg').addClass('active');
            $('.nav_menu_line').removeClass('sticky-top');
        });

        $('#overlay_bg, #close_left_sidebar').on('click', function () {
            $('#overlay_bg').removeClass('active');
            $('.nav_menu_line').addClass('sticky-top');
            $('#collapsed_menu').css('z-index', 1).animate({'left':'-280px'}, 200);
        });
    }

    return {
        init: init
    };

})(jQuery);