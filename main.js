function generateSVG() {
    var latex = document.getElementById('latex').value;

    var img = document.getElementById('img');

    img.src = 'https://detext.haskai.de/tex2svg/?latex=' + latex;

    img.width = '300';
    img.height = 'auto';
}