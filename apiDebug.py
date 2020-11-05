from flask import Flask, request
from flask_restplus import Api, Resource, fields
from flask_cors import CORS
import json
import apiprocessMSP
from apiprocessMSP import tools
from apiprocessMSP import result


app = Flask(__name__, instance_relative_config=True)
CORS(app)
apiflask = Api(app, version=apiprocessMSP.__version__, title="ApiProcess MSP")

tools.start(apiflask)
