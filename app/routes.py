from flask import jsonify, request, url_for
from app import app
import requests
# This line import your functions from the services folder
from app.services import *


@app.route("/")
def index():

    resp = """FA595 Midterm Fall 2021
    <br /><br />
    Natalia Azarian<br />
    Scott Caratozzolo<br />
    Audrey Nguyen<br />
    Agathe Sadeghi
    <br /><br />
    More information and documentation: <a href='https://github.com/scaratozzolo/FA595_Midterm'>https://github.com/scaratozzolo/FA595_Midterm</a>"""

    return resp


@app.route("/nlp", methods=["POST"])
def nlp():
    # Whatever you send to the server will then print in the console
    print(request.json)

    # Whatever you send to the server will be returned back from the api
    return jsonify(request.json)

@app.route("/nlp/services", methods=["GET", "POST"])
def services():

    __services = {
                "all": all_service,
                "chat_bot": chat_bot_service,
                "next_word": next_word_service,
        }

    if request.method == "GET":
        return jsonify({"services": {k:url_for(v.__name__) for k,v in __services.items()}})

    elif request.method == "POST":

        data = request.json

        if "services" not in data:
            return jsonify({"error": "no services defined in request"})

        response = {}

        for service in data['services']:

            if service in __services:

                response[service] = __services[service](data).get_json()

        return jsonify(response)

@app.route("/nlp/services/all", methods=["POST"])
def all_service(data=None):

    if not data:
        data = request.json
        if not data:
            return jsonify({"error":"no data provided"})

    services = {}
    services["chat_bot"] = chat_bot_service(data).get_json()
    services["next_word"] = next_word_service(data).get_json()


    return jsonify(services)

@app.route("/nlp/services/chat_bot", methods=["POST"])
def chat_bot_service(data=None):

    if not data:
        data = request.json
        if not data:
            return jsonify({"error":"no data provided"})

    chat_id = None

    if "text" not in data:
        return jsonify({"error":"'text' missing from payload"})
    elif "chat_id" in data:
        try:
            chat_id = int(data['chat_id'])
        except:
            return jsonify({"error":f"invalid 'chat_id' in payload. given: {data['chat_id']}, type: {type(data['chat_id'])}"})

    return jsonify(chat_bot(text=data['text'], chat_id=chat_id))


@app.route("/nlp/services/next_word", methods=["POST"])
def next_word_service(data=None):
    
    if not data:
        data = request.json
        if not data:
            return jsonify({"error":"no data provided"})

    k = 5
    if "text" not in data:
        return jsonify({"error":"'text' missing from payload"})
    elif "num_words" in data:
        try:
            k = int(data['num_words'])
        except:
            return jsonify({"error":f"invalid 'num_words' in payload. given: {data['num_words']}, type: {type(data['num_words'])}"})

    return jsonify(next_word(text=data['text'], k=k))