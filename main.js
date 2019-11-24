function generateSVG() {
    var latex = document.getElementById('latex').value;

    var img = document.getElementById('img');
    console.log(img);
    img.src = 'https://icatcare.org/app/uploads/2018/07/Thinking-of-getting-a-cat.png';
    img.width = '300';
    img.height = '300';
}