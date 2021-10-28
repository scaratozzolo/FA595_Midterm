# FA595_Midterm

## Deployment

Perform the following steps in a terminal or command prompt:

Clone this repo: ```git clone https://github.com/scaratozzolo/FA595_Midterm.git```

Then change directory into the repo: ```cd FA595_Midterm```

Install all the required packages: ```pip3 install -r requirements\requirements.txt```

Run the flask app: ```python3 run.py```

This will run the app on port 5000. This port must be open to incoming traffic. If the port is accepting requests, then you can use use go to http://your-public-ip:5000. If you're running the app locally, you just need to go to http://localhost:5000.

## Available Services

### GET /nlp/services

This endpoint will return a json object conatining information regarding the available services.

The services available are as follows:

 - "all" : /nlp/services/all
 - "chat_bot" : /nlp/services/chat_bot
 - "next_word" : /nlp/services/next_word

 The string in quotes can be used when defining a subset of services while perfoming a POST request on /nlp/services

### POST /nlp/services 

This endpoint allows a user to send a string of text to the server and recieve a response containing the result of calling the services specified in the payload.

The payload must contain a text of string, the subset of services as a list, as well as all of the other parameters that should be passed to each endpoint.
For example:

{"text": "your text here", "services":["chat_bot", "next_word"], "chat_id": integer, "num_words": integer}

### POST /nlp/services/all

The all endpoint allowes a user to send a string of text to the server and recieve back a response containing the result of calling all the other endpoints.

This endpoint can only be accessed through a POST request. The payload must contain a text of string as well as all of the other parameters that should be passed to each endpoint. For example:

{"text": "your text here", "chat_id": integer, "num_words": integer}

Response from the server will look like:

{
  "chat_bot": {
    ...
  }, 
  "next_word": {
    ...
  },
  ...
}

Each key in the response is equal to the values returned from /nlp/services.

### POST /nlp/services/chat_bot

The chat_bot endpoint allows a user to send a string of text to the server and recieve back a response as if you we're speaking to someone. Through the use of the chat_id in the payload, the history of the chat can be maintained and improves the response from the server.

This endpoint can only be accessed through a POST request. The payload must be in the form of one of two options: 

{"text": "your text here"} or {"text": "your text here", "chat_id": integer}

Response from the server will look like:

{"response": "chat bot response", "chat_id": integer}


### POST /nlp/services/next_word

The next_word endpoint allows a user to send a string of text to the server and recieve back a list of possible next words that would come after the submitted text. 

This endpoint can only be accessed through a POST request. The payload must be in the form of one of two options: 

{"text": "your text here"} or {"text": "your text here", "num_words": integer}

Response from the server will look like:

{'predicted_words': []}