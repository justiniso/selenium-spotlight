var message = arguments[0];

element = document.createElement("span");
element.className = 'spotlight-message';
element.innerHTML = message;
document.getElementsByTagName("body")[0].appendChild(element);