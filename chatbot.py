from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Load trained chatbot (NO TRAINING HERE)
chatbot = ChatBot(
    'SmartEduBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {'import_path': 'chatterbot.logic.BestMatch'},
        {'import_path': 'chatterbot.logic.MathematicalEvaluation'}
    ],
    database_uri='sqlite:///database.sqlite3'
)

def get_response(user_input):
    return chatbot.get_response(user_input)
