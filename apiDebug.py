from flask import Flask, request
from flask_restplus import Api, Resource, fields
from flask_cors import CORS

from apiprocessMSP import api as msptoolsapi
from apiprocessMSP import result
import json

app = Flask(__name__, instance_relative_config=True)
CORS(app)
apiflask = Api(app, version="0.1", title="ApiProcess IHCantabria")

msptoolsapi.start(apiflask)
