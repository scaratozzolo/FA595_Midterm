from flask import jsonify, request
from app import app
from app.services import *

@app.route("/nlp", methods=["POST"])
def nlp():

    return jsonify(request.json)

