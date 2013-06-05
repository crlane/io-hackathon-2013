import webapp2
import json
import urllib2
import logging as log

from google.appengine.api import backends

twitter_search_url = "http://search.twitter.com/search.json?q=%40{0}"

class TwitterTaskHandler(webapp2.RequestHandler):
    def get(self):
        if not backends.get_backend():
            self.error(403)
            return
        count = self._search_twitter('googleio')
        self.response.write('Updated. Got {0} tweets.'.format(count));

    def _search_twitter(self, search_term):
        url = twitter_search_url.format(search_term)

        tweets = []
        try:
            response = json.load(urllib2.urlopen(url))
            tweets = response['results']
        except ValueError:
            log.error('Could not parse Twitter search response')
        except KeyError:
            log.error('No field "results" in Twitter response')

        tweet_count = len(tweets)
        log.info('Found {0} matching tweets'.format(tweet_count))
        return tweet_count
