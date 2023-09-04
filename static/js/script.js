function changeImage(element) {
    var largeImage = document.getElementById("largeImage");
    largeImage.src = element.src;
}



document.querySelectorAll('.dropdown-item').forEach(function (item) {
    item.addEventListener('click', function (e) {
        e.preventDefault();
        var languageCode = this.getAttribute('data-language-code');
        document.getElementById('language-code-input').value = languageCode;
        document.getElementById('language-switch-form').submit();
    });
});

