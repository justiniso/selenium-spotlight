var CLASS = "spotlight-highlight";
var element = arguments[0];
var offset = element.getBoundingClientRect();

var highlight = document.createElement("div");
highlight.className = CLASS;

highlight.style.left = offset.left + "px";
highlight.style.top = offset.top + "px";
highlight.style.width = offset.width + "px";
highlight.style.height = offset.height + "px";

document.getElementsByTagName("body")[0].appendChild(highlight);
