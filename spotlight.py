from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener


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

    def display_message(self, message):
        with open('./message.css') as f:
            css = f.read()
        self.execute_javascript_file('./injectMessage.js', message)
        self.execute_javascript_file('./injectCss.js', css)


