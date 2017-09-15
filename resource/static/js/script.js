/**
 * Created by haizhi on 2017/8/24.
 */

function alert(message, level) {
    level = typeof level !== 'undefined' ?  level : "danger";
    var el = $('.alert');
    $('.alert-message').html(message);
    el.addClass('alert-' + level);
    el.show();
}

$(document).ready(
    function () {
        $('#alert').hide();

        $('#alert-close').click(function () {
            $(this).parent().hide();
        });
    }
);