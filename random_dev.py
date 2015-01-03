import os
import urllib
import logging
import ssl
import webapp2
import random
import binascii
from google.appengine.api import users
from google.appengine.ext import ndb
from google.appengine.api import memcache
from models import Stats

MAX_COUNT = 4096
DEFAULT_COUNT = 512
DEFAULT_ENTROPY = 4096*4;

class PersistentEntropy(object):

    def __init__(self):
        self.KEY='entropy'

    def get(self):
        val = memcache.get(self.KEY)
        if val is not None:
            return val
        else:
            stat = Stats.query(Stats.key==self.KEY).get()
            if stat is not None:
                memcache.set(key=self.KEY, value=stat.val)
                return stat.val
        return DEFAULT_COUNT

    def set(self, val):
        memcache.set(key=self.KEY, value=val)

    def delta(self, diff):
        val = memcache.get(self.KEY)
        if val is None:
            stat = Stats.query(Stats.key==self.KEY).get()
            if stat:
                val = stat.val
        if val is None:
            val = DEFAULT_COUNT
        memcache.set(key=self.KEY, value=val + diff)


pentropy = PersistentEntropy()

class EntropyCount(object):

    def __init__(self, val=DEFAULT_ENTROPY):
        self.count = val

    def get(self):
        return self.count

    def set(self, val):
        self.count = val

    def delta(self, diff):
        self.count += diff
        self.count = max(self.count, 0)
        logging.info(self.count)

entropy = EntropyCount(DEFAULT_ENTROPY)

class RandomDevice(webapp2.RequestHandler):

    def _entropy_device(self):
        return entropy

    def _entropy_count(self):
        return self._entropy_device().get()

    def get(self):
        logging.info(self.request.path)
        if self.request.path == '/dev/urandom':
            self.urandom()
        elif self.request.path == '/dev/random':
            self.random()

    def post(self):
        # 202 Accepted
        self.abort(202)

    def _parse_arguments(self):
        return type('Params',(),{
            'count': min(self.request.get('count', DEFAULT_COUNT), MAX_COUNT),
            'io': self.request.get('io', 'text'),
            'non_block': self.request.get('non_block', False),
        })

    def urandom(self):
        params = self._parse_arguments()
        self._serve(params)
        # /dev/urandom doesn't change entropy pool

    def random(self):
        params = self._parse_arguments()
        if params.count > self._entropy_count():
            if params.non_block:
                # Service unavailable
                self.abort(503)
            else:
                # Timeout to simulate block
                return
        self._serve(params)
        # /dev/random decreases entropy
        self._entropy_device().delta(-params.count)

    def _serve(self, params):
        data = os.urandom(params.count)
        if params.io == 'binary':
            self.response.headers['Content-Type'] = 'application/octet-stream; charset=binary'
            logging.info(self.response.content_type_params)
            self.response.write(data)
        else:
            self.response.headers['Content-Type'] = 'text/plain'
            self.response.write(binascii.hexlify(data))

class IoctlRandom(webapp2.RequestHandler):

    def _entropy(self):
        return entropy

    def _privileged(self):
        return (users.is_current_user_admin() or
        'X-AppEngine-Cron' in self.resquest.headers)

    def get(self):
        self._serve()

    def post(self):
        self._serve()

    def _serve(self):
        #  ['', 'ioctl', '12', 'ABC', '12', '']
        vals = self.request.path.split('/')
        logging.info(vals)
        action = vals[3]
        if action == 'RNDGETENTCNT':
            self.response.headers['Content-Type'] = 'text/plain'
            self.response.out.write(self._entropy().get())
        elif action == 'RNDADDTOENTCNT':
            try:
                count = int(vals[4])
                self._entropy().delta(count)
                # Success
                self.abort(200)
            except ValueError:
                # Bad Request
                self.abort(400)
        elif action == 'RNDGETPOOL':
            # Removed in Linux 2.6.9
            self.abort(410)
        elif action in ['RNDADDENTROPY', 'RNDZAPENTCNT', 'RNDCLEARPOOL']:
            self._entropy().delta(random.randint(0,50))
            self.abort(200)
        
