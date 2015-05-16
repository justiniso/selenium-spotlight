
var css = arguments[0];

var style = document.createElement('style');
style.type = 'text/css';
style.innerHTML = css;
document.getElementsByTagName("head")[0].appendChild(style);