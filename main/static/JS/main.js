$(document).ready(function () {
    $(".header__responsive__registration__menu").click(function () {
        $(".header__responsive__main").fadeToggle(500);
    });
});

$(document).ready(function () {
    $('.popup-with-form').magnificPopup({
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

let inputs = document.querySelectorAll('.registration__form__input');
let registration_form = document.querySelector('.registration__form');
let pass = document.querySelector('#pass');
let repass = document.querySelector('#repass');



registration_form.onsubmit = function (e) {
    let error = false;
    for (var i = 0; i <= inputs.length; i++) {
        if (inputs[i].value == "") {
            inputs[i].classList.add("form__error");
            inputs[i].classList.remove("registration__form__input__border");
        }
        e.preventDefault();
        if (pass.value != repass.value) {
            e.preventDefault();
        }
    }
}


for (var i = 0; i <= inputs.length; i++) {
    inputs[i].oninput = function () {
        if (this.classList.contains("form__error")) {
            this.classList.remove("form__error");
            this.classList.add("registration__form__input__border");
        }
    }
};