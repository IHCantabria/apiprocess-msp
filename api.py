from flask import Flask, request
from flask_restplus import Api, Resource, fields
import apiprocessMSP
from apiprocessMSP import tools
from flask_cors import CORS


app = Flask(__name__, instance_relative_config=True)
CORS(app)
apiflask = Api(app, version=apiprocessMSP.__version__, title="ApiProcess MSP")


def create():
    tools.start(apiflask)
    return app


if __name__ == "apiprocess-msp":
    create()
