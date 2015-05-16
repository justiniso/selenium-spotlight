
var CLASS = 'spotlight-message';

var existing = document.getElementsByClassName(CLASS);
for (var i = 0; i < existing.length; i++) {
    existing[i].parentNode.removeChild(existing[i]);
}
