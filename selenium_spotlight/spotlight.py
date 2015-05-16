import os
from selenium.webdriver.support.abstract_event_listener import AbstractEventListener

current_dir = os.path.dirname(os.path.realpath(__file__))

# All template files
css_injection_js = os.path.join(current_dir, 'static', 'js', 'injectCss.js')
message_css_file = os.path.join(current_dir, 'static', 'css', 'message.css')
message_injection_file = os.path.join(current_dir, 'static', 'js', 'messageDisplay.js')
message_cleanup_file = os.path.join(current_dir, 'static', 'js', 'messageCleanup.js')
highlight_css_file = os.path.join(current_dir, 'static', 'css', 'highlight.css')
highlight_element_file = os.path.join(current_dir, 'static', 'js', 'highlightElement.js')
highlight_cleanup_file = os.path.join(current_dir, 'static', 'js', 'highlightCleanup.js')


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

    def display_message(self, message):
        """Display a message in the browser window for debugging purposes"""

        with open(message_css_file) as f:
            css = f.read()
        self.execute_javascript_file(message_injection_file, message)
        self.execute_javascript_file(css_injection_js, css)

    def highlight_element(self, element):
        """Display a colored box around an element"""

        with open(highlight_css_file) as f:
            css = f.read()

        self.cleanup_highlight()
        self.execute_javascript_file(highlight_element_file, element)
        self.execute_javascript_file(css_injection_js, css)

    def cleanup_highlight(self):

        self.execute_javascript_file(highlight_cleanup_file)


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