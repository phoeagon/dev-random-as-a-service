from google.appengine.ext import ndb

class Stats(ndb.Model):
    key=ndb.StringProperty()
    val=ndb.StringProperty()
