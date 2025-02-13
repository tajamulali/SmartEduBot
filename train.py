from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
import os

# Initialize ChatBot (training mode)
chatbot = ChatBot(
    'SmartEduBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
)

# Trainers
list_trainer = ListTrainer(chatbot)
corpus_trainer = ChatterBotCorpusTrainer(chatbot)

# Load dataset.txt (if available)
dataset_path = "dataset.txt"
if os.path.exists(dataset_path):
    with open(dataset_path, "r", encoding="utf-8") as file:
        conversation = [line.strip() for line in file.readlines() if line.strip()]
        if conversation:
            print("Training chatbot with dataset.txt...")
            list_trainer.train(conversation)

# Train with built-in ChatterBot corpus
print("Training chatbot with ChatterBot corpus...")
corpus_trainer.train("chatterbot.corpus.english")

print("Training complete! Responses are saved in database.sqlite3")
