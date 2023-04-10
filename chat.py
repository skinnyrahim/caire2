pip install git+git://github.com/gunthercox/ChatterBot.git@maste
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chatbot instance
chatbot = ChatBot('MyChatbot')

# Train the chatbot with some sample conversations
trainer = ListTrainer(chatbot)
trainer.train([
    'Hello',
    'Hi there!',
    'How are you?',
    'I\'m doing great.',
    'That is good to hear.',
    'Thank you',
    'You\'re welcome.'
])

# Function to get a response from the chatbot
def get_chatbot_response(user_message):
    # Get the chatbot's response to the user's message
    bot_response = chatbot.get_response(user_message)
    
    # Return the bot response
    return str(bot_response)
