# FA595_Midterm

## Available Services

Available services can get found by performing a GET request on /nlp/services. 

The services available are as follows:

 - /nlp/services/chat_bot
 - /nlp/services/next_word



#### /nlp/services/chat_bot

The chat_bot endpoint allows a user to send a string of text to the server and recieve back a response as if you we're speaking to someone. Through the use of the chat_id in the payload, the history of the chat can be maintained and improves the response from the server.

This endpoint can only be accessed through a POST request. The payload must be in the form of one of two options: 

{"text": "your text here"} or {"text": "your text here", "chat_id": integer}

Response from the server will look like:

{"response": "chat bot response", "chat_id": integer}


#### /nlp/services/next_word

The next_word endpoint allows a user to send a string of text to the server and recieve back a list of possible next words that would come after the submitted text. 

This endpoint can only be accessed through a POST request. The payload must be in the form of one of two options: 

{"text": "your text here"} or {"text": "your text here", "num_words": integer}

Response from the server will look like:

{'predicted_words': []}