import os
from selenium.webdriver.support.abstract_event_listener import AbstractEventListener

current_dir = os.path.dirname(os.path.realpath(__file__))

# All template files
css_file = os.path.join(current_dir, 'static', 'css', 'spotlight.css')
js_file = os.path.join(current_dir, 'static', 'js', 'spotlight.js')


class JavascriptFileMixin(object):

    def execute_javascript_file(self, filename, *args, **kwargs):
        """Executes javascript in a file. You can pass any arguments using the "arguments"
        keyword. e.g.

            >>> var firstName = arguments[0];
            >>> var lastName = arguments[1];
            >>> alert("Your name is " + firstName + " " + lastName);
        """

        with open(filename) as f:
            contents = f.read()

        return self.execute_script(contents, *args, **kwargs)


class SpotlightMixin(JavascriptFileMixin):
    """Mixin to display visual feedback while Selenium is running"""

    def inject_spotlight(self):
        with open(css_file) as f:
            css = f.read()
        self.execute_javascript_file(js_file)
        self.execute_script('window.spotlight.injectCss(arguments[0])', css)

    def display_message(self, message):
        """Display a message in the browser window for debugging purposes"""
        self.inject_spotlight()
        self.excute_script('window.spotlight.dislayMessage(arguments[0])', message)

    def highlight_element(self, element):
        """Display a colored box around an element"""
        self.inject_spotlight()
        self.execute_script('window.spotlight.highlightElement(arguments[0])', element)

    def cleanup_highlight(self):
        self.inject_spotlight()
        self.execute_script('window.spotlight.removeElementsByClass(window.spotlight.highlightClass)')


class SpotlightListener(AbstractEventListener):

    def on_exception(self, exception, driver):
        """Display the exception on the screen"""
        driver.display_message(str(exception))

    def before_click(self, element, driver):
        """Highlight the element"""
        driver.highlight_element(element)

    def after_click(self, element, driver):
        """Remove the highlight"""
        driver.cleanup_highlight()