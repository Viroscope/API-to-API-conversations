# API to API Conversations

This code implements a conversational AI chatbot using the OpenAI GPT-3.5 Turbo model. The chatbot simulates a conversation between two characters, Karen and Charles, who have distinct personalities. Karen is sarcastic, while Charles is also sarcastic but in a different way. The chatbot alternates between Karen and Charles, generating responses based on the conversation history.

## Prerequisites

Before running the code, make sure you have the following dependencies installed:

- Python 3.x
- `requests` library
- `dotenv` library

You also need to obtain an API key from OpenAI to access the GPT-3.5 Turbo model.

## Setup

1. Clone the repository and navigate to the project directory.

2. Install the required dependencies using the following command:
   ```
   pip install requests python-dotenv
   ```

3. Create a file named `.env` in the project directory and add your OpenAI API key to it in the following format:
   ```
   OpenAIKey=YOUR_API_KEY
   ```

## Usage

The main part of the code simulates a conversation between Karen and Charles. Each character takes turns generating responses based on the conversation history.

To run the code, execute the following command:
```
python chatbot.py
```

## Code Explanation

### Importing Dependencies

The required libraries are imported at the beginning of the code:
- `requests` is used to make HTTP requests to the OpenAI API.
- `os` is used to access the environment variables.
- `json` is used to parse and format JSON data.
- `time` is used to introduce delays between conversation turns.
- `dotenv` is used to load environment variables from the `.env` file.

### Loading Environment Variables

The code uses the `dotenv_values` function from the `dotenv` library to load environment variables from the `.env` file. The API key is stored in the `apiKey` variable.

### Defining Conversation Roles

Two functions, `Charles` and `Karen`, are defined to generate responses from the respective characters. These functions take the API key and the conversation history as input.

The conversation history is a list of messages, where each message has a role (`user`, `assistant`, or `system`) and content (the text of the message).

### Generating Responses

Inside the `Charles` and `Karen` functions, the API endpoint URL and headers are set. The conversation history is modified to include system messages that provide role-playing instructions to the characters. The conversation history is then sent as a JSON payload to the OpenAI API using a POST request.

The response from the API is parsed as JSON, and the generated response from the character is extracted from the response data.

### Running the Conversation Loop

The main part of the code executes a loop that simulates the conversation. In each iteration, Karen and Charles take turns generating responses.

- Karen generates a response using the `Karen` function and prints it in pink color.
- The generated response from Karen is added to the conversation history with the role set as `user`.
- A 1-second pause is introduced.
- Charles generates a response using the `Charles` function and prints it in blue color.
- The generated response from Charles is added to the conversation history with the role set as `assistant`.
- Another 1-second pause is introduced.
- A new line is printed to separate the outputs of each iteration.

## Note

The code includes commented-out lines that print the JSON responses from the OpenAI API. Uncommenting these lines can be useful for debugging or inspecting the response data structure.
