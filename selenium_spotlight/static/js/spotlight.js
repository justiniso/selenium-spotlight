
window.spotlight = {

    cssClass: 'spotlight-css',
    messageClass: 'spotlight-message',
    highlightClass: 'spotlight-highlight',
    crosshairsClass: 'spotlight-crosshair',

    /**
     *   Inject CSS rules into the page
     */
    injectCss: function (css) {
        var style = document.createElement('style');

        style.className = this.cssClass;
        style.type = 'text/css';
        style.innerHTML = css;
        document.getElementsByTagName("head")[0].appendChild(style);
    },

    /**
     *   Display a message in the window
     */
    displayMessage: function (message) {
        element = document.createElement("span");
        element.className = this.messageClass;
        element.innerHTML = message;
        document.getElementsByTagName("body")[0].appendChild(element);
    },

    /**
     *   Utility function to remove elements
     */
    removeElementsByClass: function (className) {
        var existing = document.getElementsByClassName(className);
        for (var i = 0; i < existing.length; i++) {
            existing[i].parentNode.removeChild(existing[i]);
        }
    },

    /**
     *   Overlay a transparent element on top of the specified element
     */
    highlightElement: function (element) {
        var offset = element.getBoundingClientRect();

        var highlight = document.createElement("div");
        highlight.className = this.highlightClass;

        highlight.style.left = offset.left + "px";
        highlight.style.top = offset.top + "px";
        highlight.style.width = offset.width + "px";
        highlight.style.height = offset.height + "px";

        document.getElementsByTagName("body")[0].appendChild(highlight);
    }
};