import os
import urllib
import logging

from google.appengine.api import users
from google.appengine.ext import ndb

import jinja2
import webapp2
from random_dev import RandomDevice
from random_dev import IoctlRandom
from random_dev import CronJobHandler
from random_dev import ProcFS

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class MainPage(webapp2.RequestHandler):

    def get(self):
        self.redirect('http://phoeagon.github.io/dev-random-as-a-service/')

class Login(webapp2.RequestHandler):

    def get(self):
        self.redirect(users.create_login_url('/'))

class Logout(webapp2.RequestHandler):

    def get(self):
        self.redirect(users.create_logout_url('/'))

application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/login', Login),
    ('/logout', Logout),
    ('/dev/null', RandomDevice),
    ('/dev/zero', RandomDevice),
    ('/dev/urandom', RandomDevice),
    ('/dev/random', RandomDevice),
    (r'/ioctl/[0-9]+/[A-Z]+/[A-Za-z0-9]+/', IoctlRandom),
    ('/_cron/flush', CronJobHandler),
    ('/proc/sys/kernel/random/entropy_avail', ProcFS),
], debug=True)
