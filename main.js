function generateSVG() {
    var latex = document.getElementById('latex').value;

    var img = document.getElementById('img');

    img.src = 'https://detext.haskai.de/tex2svg/?latexB64=' + btoa(latex);
}