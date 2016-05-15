/**
 * Created by root on 5/15/16.
 */
$(document).ready(function () {
    if(u){
        var al = $(".lock");
        $(al[0]).attr("href", "/center");
        $(al[0]).html(u);
        $(al[1]).attr("href", "/logout");
        $(al[1]).html("Logout");
    }
});
