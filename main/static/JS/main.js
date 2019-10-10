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
