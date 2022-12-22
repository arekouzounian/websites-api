#!/usr/bin/python

import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "/var/www/api.arekouzounian.com")

from websites_api import create_app

application = create_app()
