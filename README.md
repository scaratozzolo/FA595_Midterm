# FA595_Midterm

## Available Services

Available services can get found by performing a GET request on /nlp/services. A POST request on this endpoint will produce different results. More info below.

The services available are as follows:

 - /nlp/services/all
 - /nlp/services/chat_bot
 - /nlp/services/next_word

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