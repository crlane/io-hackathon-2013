# Batch processing task URL routes
# These should not be configured to be public, but only
# available through private backends, requiring admin login.
import webapp2
from config import config
from webapp2_extras import routes

urls = [
    routes.RedirectRoute(r'/tasks/twitter', handler='task_handlers.TwitterTaskHandler',
        strict_slash=True, name='twitter-task'),
]

app = webapp2.WSGIApplication(urls, config=config.config,debug=True)
