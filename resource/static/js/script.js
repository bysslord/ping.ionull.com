/**
 * Created by haizhi on 2017/8/24.
 */

function alert(level, title, message) {
    var el = $('.alert');
    $('.alert-title').html(title);
    $('.alert-message').html(message);
    el.addClass('alert-' + level);
    el.show();
}

$(document).ready(
    function () {
        // $('#alert').hide();

        $('#alert').click(function () {
            alert('warning', '错误', '对不起...');
        });

        $('#alert-close').click(function () {
            $(this).parent().hide();
        });

        $('#icon-json').click(function () {
            Sijax.request('json', [$('#connector_id').val()])
        });
    }
);