/**
 * Created by root on 5/15/16.
 */
$(document).ready(function () {
    var status_email = false;
    var status_pwd = false;
    $("#email-ipt").blur(function () {
        var email = $(this).val();
        var ee = $(".email-error");
        if (email.length < 1) {
            $(ee).html("用户名为空！")
        } else {
            $.ajax({
                type: "POST",
                url: "/user_login/",
                data: {"email": email},
                dataType: "json",
                cache: false,
                success: function (ret) {
                    if (ret == 0) {
                        status_email = false
                        $(ee).html("用户不存在！")
                    } else {
                        status_email = true;
                        $(ee).html("√");
                        $(ee).css("color", "green")
                    }
                }
            })
        }

    });
    $("#pwd-ipt").blur(function () {
        var pwd = $(this).val();
        var email = $("#email-ipt").val();
        var pe = $(".pwd-error");
        var ee = $(".email-error");
        if (pwd.length < 1) {
            $(pe).html("密码为空！")
        } else if (status_email) {
            $.ajax({
                type: "POST",
                url: "/test_pwd/",
                data: {"password": pwd, "email": email},
                dataType: "json",
                cache: false,
                success: function (ret) {
                    if (ret == 1) {
                        status_pwd = true;
                        $(pe).html("√");
                        $(pe).css("color", "green")
                    } else {
                        status_pwd = false;
                        $(pe).html("密码不正确！");
                    }
                }
            })
        } else {
            $(ee).html("用户名为空！")
            $(ee).css("color", "red")
        }
    });
    $("#login-form").submit(function () {
        return status_email && status_pwd
    })
});