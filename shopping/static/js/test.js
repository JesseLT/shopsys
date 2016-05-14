/**
 * Created by root on 5/14/16.
 */
$(document).ready(function () {
    $("#btn").click(function () {
        var content = $("#test").val()
        $.ajax({
            type: "POST",
            url: "/test_ajax",
            data: {"value": content},
            dataType: "json",
            cache: false,
            success: function (ret) {
                alert(ret)
            },
            error: function () {
                alert("error")
            }
        })

    })
});
