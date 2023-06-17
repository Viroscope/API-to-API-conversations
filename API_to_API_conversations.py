import requests
import os
import json
import time

from dotenv import dotenv_values

env_values = dotenv_values(".env")
apiKey = env_values["OpenAIKey"]

# ANSI escape sequences for text coloring
PINK = '\033[95m'
BLUE = '\033[94m'
RESET = '\033[0m'

def Charles(apiKey, conversation):
    apiUrl = 'https://api.openai.com/v1/chat/completions'

    messages = conversation + [
        {
            'role': 'system',
            'content': 'You are roleplaying as a pretty sarcastic person. You are not AI just saracastic Charles. Stay in character and keep the conversation going.'
        },
        {
            'role': 'user',
            'content': conversation[-1]['content'] if conversation and 'content' in conversation[-1] else ''
        }
    ]

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + apiKey
    }

    data = {
        'messages': messages,
        'max_tokens': 600,
        'temperature': 0.8,  # Set temperature to 0.8
        'model': 'gpt-3.5-turbo'
    }

    response = requests.post(apiUrl, headers=headers, json=data)
    response_data = response.json()

    charles_speaks = response_data['choices'][0]['message']['content'].strip()
    return charles_speaks, response_data

def Karen(apiKey, conversation):
    apiUrl = 'https://api.openai.com/v1/chat/completions'

    messages = conversation + [
        {
            'role': 'system',
            'content': 'You are roleplaying as a pretty sarcastic person. You are not AI just saracastic Karen. Stay in character and keep the conversation going.'
        },
        {
            'role': 'assistant',  # Set role as assistant for Karen
            'content': conversation[-1]['content'] if conversation and 'content' in conversation[-1] else ''
        }
    ]

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + apiKey
    }

    data = {
        'messages': messages,
        'max_tokens': 600,
        'temperature': 0.8,  # Set temperature to 0.8
        'model': 'gpt-3.5-turbo'
    }

    response = requests.post(apiUrl, headers=headers, json=data)
    response_data = response.json()

    karen_speaks = response_data['choices'][0]['message']['content'].strip()
    return karen_speaks, response_data

conversation = []

for _ in range(20):
    karen, karen_response = Karen(apiKey, conversation)
    print(f"{PINK}Karen: {karen}{RESET}")
    #print("Karen Response JSON:")
    #print(json.dumps(karen_response, indent=2))

    conversation.append({'role': 'user', 'content': karen})  # Set role as user for Karen's response

    time.sleep(1)  # Pause for 1 second

    charles, charles_response = Charles(apiKey, conversation)
    print(f"{BLUE}Charles: {charles}{RESET}")
    #print("Charles Response JSON:")
    #print(json.dumps(charles_response, indent=2))

    conversation.append({'role': 'assistant', 'content': charles})  # Set role as assistant for Charles's response

    time.sleep(1)  # Pause for 1 second

    print()  # Add a new line between outputs
