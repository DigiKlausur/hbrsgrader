from .base import BaseApiHandler
from tornado import web
import sys
import glob
import json

class GraderBaseHandler(BaseApiHandler):

    def initialize(self):
        path = '{}/share/grader/*.json'.format(sys.prefix)
        self.grader_config = {
            "graders": []
        }
        filenames = glob.glob(path)
        for filename in filenames:
            try:
                with open(filename, 'r') as f:
                    json_grader = json.loads(f.read())
                    self.grader_config["graders"].append(json_grader)
            except:
                print('Error loading config file at {}!'.format(filename)) 

    @web.authenticated
    def get(self):
        self.write(json.dumps(self.grader_config))

default_handlers = [
    (r'/grader/api/base', GraderBaseHandler)
]