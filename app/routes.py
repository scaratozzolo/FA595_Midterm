from flask import jsonify, request
from app import app
# This line import your functions from the services folder
from app.services import *


@app.route("/")
def index():

    return "Hello World"


@app.route("/nlp", methods=["POST"])
def nlp():
    # Whatever you send to the server will then print in the console
    print(request.json)

    # Whatever you send to the server will be returned back from the api
    return jsonify(request.json)

