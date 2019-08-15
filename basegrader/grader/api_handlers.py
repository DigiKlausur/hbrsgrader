from .base import BaseApiHandler
from tornado import web
import sys
import json

class GraderBaseHandler(BaseApiHandler):

    def initialize(self):
        self.path = '{}/share/grader/config.json'.format(sys.prefix)
        self.grader_config = dict()
        with open(self.path, 'r') as f:
            self.grader_config = json.loads(f.read())        

    @web.authenticated
    def get(self):
        self.write(json.dumps(self.grader_config))

default_handlers = [
    (r'/grader/api/base', GraderBaseHandler)
]