import webapp2

import json
import urllib2
import logging as log
from twitter import *

def _get_api_access_keys():
    """Returns a dictionary with key-value pairs for TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET, 
    TWITTER_ACCESS_TOKEN, and TWITTER_ACCESS_TOKEN_SECRET for current
        service provider. Must return (key, secret), order *must* be respected.
        """
    app = webapp2.get_app()
    return app.config.get('TWITTER_API_CRED')

class TwitterTaskHandler(webapp2.RequestHandler):

    def __init__(self, request, response):
        self.initialize(request, response)
        self.t = None
        cred = _get_api_access_keys()
        try:
            self.t = Twitter(auth=OAuth(cred['TWITTER_ACCESS_TOKEN'], cred['TWITTER_ACCESS_TOKEN_SECRET'],\
                           cred['TWITTER_CONSUMER_KEY'], cred['TWITTER_CONSUMER_SECRET']))
        except TwitterError as e:
            log.error('Could not connect to twitter api: {0}'.format(e))
        except NameError,KeyError:
            log.error('Failed to properly load twitter api credentials')

    def get(self):
        if self.t:
            count = self._search_twitter(term='googleio')
            self.response.write('Updated. Got {0} tweets.'.format(count));
        else: 
            self.response.write('No twitter api connection, query not performed');

    def _search_twitter(self, term):
        statuses = []
        try: 
            statuses = self.t.search.tweets(q=term)
        except TwitterError as e:
            log.error('Failed to get results from twitter search: {0}'.format(e))

        tweet_count = len(statuses)
        log.info('Found {0} matching tweets'.format(tweet_count))
        return tweet_count

