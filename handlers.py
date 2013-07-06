import webapp2
import jinja2
import string
import json

_JINJA = jinja2.Environment(
        loader=jinja2.FileSystemLoader('templates/'),
        extensions=['jinja2.ext.autoescape'])

class IndexHandler(webapp2.RequestHandler):
    def get(self):
        msg = 'Welcome to Google I/O Extended Atlanta 2013'
        template = _JINJA.get_template('index.html')
        self.response.write(template.render(message=msg))

class TwitterDisplayHandler(webapp2.RequestHandler):
    def get(self):
        # right now, twitter_data is a dict
        twitter_data = json.dumps(dict(zip([a for a in string.ascii_lowercase[:10]], xrange(2,12))))
        template = _JINJA.get_template('twitterdisplay.html')
        self.response.write(template.render(twitter_data = twitter_data))
