/**
 * Created by haizhi on 2017/8/24.
 */
function executeFinished() {
    $('#execute').removeClass('is-loading');
}


function renderJson(data) {
    console.info(data);
    $("#result").JSONView(data);
}


$(document).ready(
    function () {
        $('#execute').click(function () {
            $('#execute').addClass('is-loading');
            Sijax.request('execute', [$('#connector_id').val(), $('#sql').val()]);
        });

        $('#icon-json').click(function () {
            Sijax.request('json', [$('#connector_id').val()])
        });
    }
);