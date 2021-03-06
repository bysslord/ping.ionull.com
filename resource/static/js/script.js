/**
 * Created by haizhi on 2017/8/24.
 */

function alert(message, level) {
    level = typeof level !== 'undefined' ?  level : "danger";
    var el = $('.alert');
    $('.alert-message').html(message);
    el.addClass('alert-' + level);
    el.slideDown();

    setTimeout(function () {
        el.slideUp()
    }, 2000)
}

var log = {};
log.info = function (message) {
    $.post('/log/info', {message: message})
};

log.error = function (message) {
    $.post('/log/error', {message: message})
};

$(document).ready(
    function () {
        $('#alert').hide();

        $('#alert-close').click(function () {
            $(this).parent().slideUp();
        });
    }
);