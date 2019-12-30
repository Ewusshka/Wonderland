google.load("language", "1");

function initialize() {
    var content = document.getElementById('content');
    content.innerHTML = '<div id="text">Hola, me alegro mucho de verte.<\/div><div id="translation"/>';
    var text = document.getElementById("text").innerHTML;
    google.language.translate(text, 'sk', 'cz', function(result) {
        var translated = document.getElementById("translation");
        if (result.translation) {
            translated.innerHTML = result.translation;
        }
    });
}
google.setOnLoadCallback(initialize);