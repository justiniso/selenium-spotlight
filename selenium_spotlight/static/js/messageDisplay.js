
var CLASS = 'spotlight-message';
var message = arguments[0];

var existing = document.getElementsByClassName(CLASS);

element = document.createElement("span");
element.className = CLASS;
element.innerHTML = message;
document.getElementsByTagName("body")[0].appendChild(element);
