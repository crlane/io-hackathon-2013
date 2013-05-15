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
- Installation of the Git client of your choice for your OS: http://git-scm.com/downloads
- Github Account: https://github.com/signup/free
- Github SSH setup: https://help.github.com/articles/generating-ssh-keys
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

Contributing and Particpating
-----------------------------
Anyone who has an interest should feel free to participate in the project.  Because we expect to have several people working on the code intermittently, we'll be using Github to coordinate and merge everyone's code.

If you feel comfortable with git and Github, you may simply ask the project coordinators for write-access to the repository, and you can push commits directly.

If you're less familiar with git and Github, or you'd simply like to learn one of the standard ways coders use to submit code to open-source projects on Github, use the following procedure:
- While logged into your own Github account, fork this repository to create a copy in your own account.  Simply click the "Fork" button on the upper right of the repository page.
- Clone the fork to your local development machine

    ```
    git clone git@github.com:<your github account>/io-hackathon-2013.git
    ```

- Since your own fork is now set up as the `origin` remote, you'll want to create another remote to point to the shared, original repository, to pull everyone else's changes in periodically.  Typically this is named `upstream`

    ```
    git remote add upstream https://github.com/sagepath/io-hackathon-2013.git
    ```

- Update your local repository on the master branch from the upstream remote.

    ```
    git pull upstream master
    ```

- Make your code changes.  Make sure that when you're ready to share your changes, you pull from the upstream master again and merge any changes you might have.  Pull will attempt to merge by default, but sometimes it can be better to use `git pull --rebase` to avoid conflicts and unnecessary merge commits in the history.  Feel free to ask if you need help with this step.
- Once you've merged in upstream changes with your own changes, and tested to see if things seem to be working, you're ready to share your code.  Push it up first your own fork, which should be set up as the `origin` remote.

    ```
    git push origin master
    ```

- After you've pushed to your own fork successfully, you can send the original repository a "pull request."  Simply navigate to your own forked repository page and click "Pull Request" at the top of the page.  Github should present you with the list of commits you've made and default the destination to the original repository.  Accept these options and the Pull Request will be sent to the people coordinating the original repository.

- If everything seems to be working well, the coordinators can accept your Pull Request and your changes will be incorported into the upstream repository.

- Wash, rinse, and repeat!


Reading / Documentation
-----------------------
Here are some useful links to documentation to familiarize yourself with some of the technology involved in the project.

- Python Documentation: http://docs.python.org/2/
- Google App Engine Tutorial: https://developers.google.com/appengine/docs/python/gettingstartedpython27/
- Twitter Developer Documentation: https://dev.twitter.com/start
- HTML5 Canvas Element: http://diveintohtml5.info/canvas.html
- jQuery Documentation: http://api.jquery.com/

