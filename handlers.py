import webapp2
import jinja2
import string
import json
import itertools

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
        word, weight = "name", "value"
        letters = string.ascii_lowercase[:10]
        data = []
        for i, letter in enumerate(letters):
            data.append(dict(zip([word,weight],[letter,(i+1)*1000])))
        A = dict()
        A["name"] = "ROOT"
        A["children"] = data

        twitter_data = json.dumps(A)
        template = _JINJA.get_template('twitterdisplay.html')
        self.response.write(template.render(twitter_data = twitter_data))
