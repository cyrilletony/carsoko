#!/usr/bin/env python3.9
# -*- coding: UTF-8 -*-


import os
import sys
sys.path.insert(0, "C:/Users/user/Desktop/projects/projects/carsoko/flaskapp")

from flup.server.fcgi import WSGIServer
from app import app


class ScriptNamePatch(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        environ['SCRIPT_NAME'] = ""
        return self.app(environ, start_response)

app = ScriptNamePatch(app)

if __name__ == '__main__':
    WSGIServer(app,bindAddress="test-fcgi.sock").run()