import os
import urllib
import logging

from google.appengine.api import users
from google.appengine.ext import ndb

import jinja2
import webapp2
from random_dev import RandomDevice
from random_dev import IoctlRandom

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class MainPage(webapp2.RequestHandler):

    def get(self):
        template_values = {
        }

        template = JINJA_ENVIRONMENT.get_template('templates/index.html')
        self.response.write(template.render(template_values))


application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/dev/urandom', RandomDevice),
    ('/dev/random', RandomDevice),
    (r'/ioctl/[0-9]+/[A-Z]+/[A-Za-z0-9]+/', IoctlRandom),
], debug=True)
