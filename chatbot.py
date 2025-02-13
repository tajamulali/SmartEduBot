from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Creating ChatBot Instance
chatbot = ChatBot(
    'WaibyGPT',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': "Hi there, Welcome to WaibyGPT! 👋 If you need any assistance, I'm always here.\n\nGo ahead and write the number of any query. 😃✨<br><br>\n1. Student's Section Enquiry.<br>\n2. Faculty Section Enquiry.<br>\n3. Parent's Section Enquiry.<br>\n4. Visitor's Section Enquiry.<br>",
            'maximum_similarity_threshold': 0.90
        }
    ],
    database_uri='sqlite:///database.sqlite3'  # Storing trained responses
)

# Training should be done separately in train.py, so we don't retrain on every run
if __name__ == "__main__":
    print("Chatbot is ready to serve queries!")
