import webapp2
import json
import urllib2
import logging as log
from twitter import *

KEYFILE = 'twitter_api.cfg'

def _get_api_access_keys(f=KEYFILE):
    # TODO: better solution for this, possibly using datastore
    D = {}
    with open(f, 'r') as creds: 
        for line in creds:
            key,value = [k.strip() for k in line.split(":")]
            D[("_").join([w.upper() for w in key.split()])] = value
    return D
    
class TwitterTaskHandler(webapp2.RequestHandler):

    def __init__(self, request, response):
        self.initialize(request, response)
        self.t = None
        cred = _get_api_access_keys()
        try:
            self.t = Twitter(auth=OAuth(cred['ACCESS_TOKEN'], cred['ACCESS_TOKEN_SECRET'],\
                           cred['CONSUMER_KEY'], cred['CONSUMER_SECRET']))
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

