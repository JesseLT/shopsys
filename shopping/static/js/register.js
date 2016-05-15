/**
 * Created by root on 5/13/16.
 */
$(document).ready(function () {
    var name_status = false;
    var email_status = false;
    var pwd_status = false;
    var pwdcfm_status = false;
    $("#name").blur(function () {
        var name = $(this).val();
        var error_mes = $(".name-error-mesg");
        if (name.length < 5) {
            name_status = false;
            $(error_mes).html("name长度应该大于6!");
            return false
        } else {
            name_status = true;
            $(error_mes).html("√");
            $(error_mes).css("color", "green");
        }
        if (!/^[a-zA-Z]\w+$/.test(name)) {
            name_status = false;
            $(error_mes).html("name包含非法字符！");
            return false
        } else {
            name_status = true;
            $(error_mes).html("√");
            $(error_mes).css("color", "green");
        }
    });
    $("#pwd").blur(function () {
        var password = $(this).val();
        var pwd_error_mesg = $(".pwd-error-mesg");
        if (password.length < 6) {
            pwd_status = false;
            $(pwd_error_mesg).html("密码长度应该大于6!");
            return false
        } else {
            pwd_status = true;
            $(pwd_error_mesg).html("√");
            $(pwd_error_mesg).css("color", "green");
        }
        if (!/^\w+$/.test(password)) {
            pwd_status = false;
            $(pwd_error_mesg).html("密码包含非法字符！");
            return false
        } else {
            pwd_status = true;
            $(pwd_error_mesg).html("√");
            $(pwd_error_mesg).css("color", "green");
        }
    });
    $("#email").blur(function () {
        var email = $(this).val();
        var email_re = /^\w{6,20}@\w+\.\w+$/;
        var email_error_mesg = $(".email-error-mesg");
        if (!email_re.test(email)) {
            $(email_error_mesg).html("email不合法！");
        } else {
            $.ajax({
                url: "/test_email/",
                type: "POST",
                dataType: "json",
                data: {"email": email},
                cache: false,
                success: function (ret) {
                    if (ret > 0) {
                        $(email_error_mesg).html("email已经存在！")
                    } else {
                        email_status = true;
                        $(email_error_mesg).html("√");
                        $(email_error_mesg).css("color", "green");
                    }
                }
            })
        }
    });
    $("#pwdcfm").blur(function () {
        var password1 = $("#pwd").val();
        var password2 = $(this).val();
        var pwdcfm_error_mesg = $(".pwdcfm-error-mesg");
        if (password2 == "") {
            pwdcfm_status = false;
            return false
        } else if ((password2 !== password1) && (password2 !== "")) {
            pwdcfm_status = false;
            $(pwdcfm_error_mesg).html("两次密码不一致！");
        } else {
            pwdcfm_status = true;
            $(pwdcfm_error_mesg).html("√");
            $(pwdcfm_error_mesg).css("color", "green")
        }
    });
    $("#register-form").submit(function () {
        return name_status && pwd_status && email_status && pwdcfm_status
    });

});