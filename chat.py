import json

# Load the chatbot data from a JSON file
with open('chatbot_data.json', 'r') as file:
    chatbot_data = json.load(file)

# Define a function to get a response from the chatbot
def get_chatbot_response(user_message):
    # Check if the user's message is in the chatbot data
    if user_message in chatbot_data:
        # If so, return the corresponding response
        return chatbot_data[user_message]
    else:
        # If not, return a default response
        return 'I\'m sorry, I didn\'t understand that.'

