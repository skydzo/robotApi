#!/usr/bin/python3

import logging
import sys
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/var/www/html/robotApi/')
from ab_flask.sample_flask import app as application
application.secret_key = '123'