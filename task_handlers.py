import webapp2

class TwitterTaskHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Updated.');

