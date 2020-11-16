#!/usr/bin/python
# virtualenv api
activate_this = "/var/www/msp/env/bin/activate_this.py"
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))
import sys
import logging

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "/var/www/msp")

# from FlaskApp import app as application
import api

# api = Api()
application = api.create()
