#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import urllib2
import json

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('<h1>Welcome to Google I/O Extended Atlanta 2013</h1>')

#JR - Here is what I came up with for the twitter search and parse. I’m not sure how
#to plug this into the webapp2. I’ll keep plugging away. Thanks for setting this up.
#Joe Reed - 05/16/13
#TwitterSearchURL = "http://search.twitter.com/search.json?q=%40mollywood"
#
#response = json.load(urllib2.urlopen(TwitterSearchURL))
#
#NumberOfTweets = len(response['results'])
#
#if NumberOfTweets < 1:
#	print "No Tweets Found..."
#else:
#	for x in range(0, NumberOfTweets):
#		try:
#			print response['results'][x]['from_user']
#			print response['results'][x]['from_user_name']
#			print response['results'][x]['created_at']
#			print response['results'][x]['text']
#		except:
#			print "Error while trying to print Tweets..."

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
