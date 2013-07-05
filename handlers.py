import webapp2
import jinja2

_JINJA = jinja2.Environment(
        loader=jinja2.FileSystemLoader('templates/'),
        extensions=['jinja2.ext.autoescape'])

class IndexHandler(webapp2.RequestHandler):
    def get(self):
        msg = 'Welcome to Google I/O Extended Atlanta 2013'
        template = _JINJA.get_template('index.html')
        self.response.write(template.render(message=msg))


