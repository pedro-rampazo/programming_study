// This is a native JS file
var p = document.getElementsByTagName('p');

alert(p.length); // <p> quantity in HTML
alert(p[0]); // data type in HTML document
alert(p[0].innerHTML); // data content in HTML document
p[0].innerHTML = "Olá Mundo!!"; // change content in index 0