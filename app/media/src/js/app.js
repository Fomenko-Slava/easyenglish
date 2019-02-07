var app = app || {};

app.app = (function($, app){

    function init () {
        app.plugins.init();

        switch (app.CUR_PAGE) {
            case 'main':
                //app.main_page.init();
                break;
        }
    }

    return {
        init: init
    };
})(jQuery, app);

// точка входа, запускаем все скрипты
$(function() {
    app.app.init();
});