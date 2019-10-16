$(document).ready(function () {
    $(".header__responsive__registration__menu").click(function () {
        $(".header__responsive__main").fadeToggle(500);
    });
});

$(document).ready(function () {
    $('.login_btn').magnificPopup({
        type: 'inline',
        preloader: false,
        focus: '#name',

        // When elemened is focused, some mobile browsers in some cases zoom in
        // It looks not nice, so we disable it:
        callbacks: {
            beforeOpen: function () {
                if ($(window).width() < 700) {
                    this.st.focus = false;
                } else {
                    this.st.focus = '#name';
                }
            }
        }
    });
});

$(".account__menu__description__responsive__bar").click(function () {
    $(".account__menu__nav__list").fadeToggle(500);

    if ($(".arrow").hasClass("down")) {
        $(".arrow").removeClass("down").addClass("up");
    } else if ($(".arrow").hasClass("up")) {
        $(".arrow").removeClass("up").addClass("down");
    }
});


$("#id_username").addClass("registration__form__input registration__form__input__border");
$("#id_password").addClass("registration__form__input registration__form__input__border");
$("#id_password__check").addClass("registration__form__input registration__form__input__border");
$("#id_email").addClass("registration__form__input registration__form__input__border");
