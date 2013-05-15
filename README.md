io-hackathon-2013
=================

Hackathon Project for Google I/O Extended Event 2013

The Project
-----------
In keeping with the Google I/O conference theme, we're going to see what other people have to say about the event while we watch the talks and hack away.  We'll be using Google's AppEngine, part of their Cloud Platform offering, to build a Python application which can listen to posts about Google I/O on Twitter or other popular social networks.  Once we've gotten some of that data, we're going to be writing a simple front end using JavaScript and HTML5 components, such as the canvas element, to come up with interesting ways to visualize the data!

Prerequisites
-------------
Here's what you'll need to participate in the Hackathon.

- A laptop or other development machine
- Your favorite code editor/editors (For Python, HTML, JavaScript)
- Installation of Python 2.7.x for your operating system: http://www.python.org/download/releases/2.7.4/
- Installation of the Google AppEngine SDK for Python: https://developers.google.com/appengine/downloads#Google_App_Engine_SDK_for_Python
- Your favorite browser (to test / run the app)

Possible Project Components
---------------------------
Here's a potential list of the various components of the project.  This isn't a constraint for other ideas, but just a possible list of things to work on to get started.

- Google App Engine backend handler for querying Twitter, probably scheduled on a timer
- Third party library or hand-written code for querying Twitter by hashtag.
- Google DataStore models / data access code for storing Twitter data in a way that will be easy to create visualizations from.
- Google App Engine front-end REST API for querying the most recently copy of the visualization data.
- HTML5 form page for user to input hashtag to search by.
- HTML5 page with canvas element for displaying visualization.
- JavaScript / jQuery code for querying the REST API.
- JavaScript / jQuery code for doing visualization calculations.

Reading / Documentation
-----------------------
Here are some useful links to documentation to familiarize yourself with some of the technology involved in the project.

- Python Documentation: http://docs.python.org/2/
- Google App Engine Tutorial: https://developers.google.com/appengine/docs/python/gettingstartedpython27/
- Twitter Developer Documentation: https://dev.twitter.com/start
- HTML5 Canvas Element: http://diveintohtml5.info/canvas.html
- jQuery Documentation: http://api.jquery.com/

