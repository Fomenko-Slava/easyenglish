app.plugins = (function ($) {

    function init() {
        navbar_menu();
    }
    
    function navbar_menu() {
        $('[data-toggle="slide-collapse"]').on('click', function() {
            alert('123');
            $navMenuCont = $($(this).data('target'));
            $navMenuCont.animate({'width':'toggle'}, 350);
        });
    }

    return {
        init: init
    };

})(jQuery);