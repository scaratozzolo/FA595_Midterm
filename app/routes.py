from flask import jsonify, request
from torch.cuda.memory import empty_cache
from app import app
from app import services
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

@app.route("/nlp/services", methods=["GET"])
def available_services():
    
    services = {"services": {
                            "all": "/nlp/services/all",
                            "chat_bot": "/nlp/services/chat_bot",
                            "next_word": "/nlp/services/next_word",
        }
    }

    # Whatever you send to the server will be returned back from the api
    return jsonify(services)

@app.route("/nlp/services/chat_bot", methods=["POST"])
def chat_bot_service():

    data = request.json
    chat_id = None

    if "text" not in data:
        return jsonify({"error":"'text' missing from payload"})
    elif "chat_id" in data:
        try:
            chat_id = int(data['chat_data'])
        except:
            return jsonify({"error":f"invalid 'chat_id' in payload. given: {data['chat_data']}, type: {type(data['chat_id'])}"})

    return jsonify(chat_bot(text=data['text'], chat_id=chat_id))
    

