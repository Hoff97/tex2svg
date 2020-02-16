function generateSVG() {
    var latex = document.getElementById('latex').value;

    var img = document.getElementById('img');

    var url = 'https://detext.haskai.de/tex2svg/?latexB64=' + btoa(latex);
    var urlLink = url + '&scale=5';

    img.src = url;

    document.getElementById('img-href').setAttribute('href', urlLink);

    var urlText = document.getElementById('url');
    urlText.innerText = url;
    document.getElementById('result').setAttribute('style', 'visibility: visible');
}

function copyToClipBoard() {
    var latex = document.getElementById('latex').value;

    var url = 'https://detext.haskai.de/tex2svg/?latexB64=' + btoa(latex) + '&scale=5';

    navigator.clipboard.writeText(url);

    alert('Copied to clipbaord');
}