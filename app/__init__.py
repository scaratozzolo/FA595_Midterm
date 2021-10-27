from flask import Flask, jsonify, request

app = Flask(__name__)



@app.route("/nlp", methods=["POST"])
def nlp():

    return jsonify(request.json)