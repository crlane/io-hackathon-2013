import webapp2

class IndexHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('<h1>Welcome to Google I/O Extended Atlanta 2013</h1>')


