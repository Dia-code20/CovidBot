
from chatterbot import ChatBot
import chatterbot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

#création d'une instance de chatbot

chatbot = ChatBot(
    'Chatty',
    storage_adapter= 'chatterbot.storage.SQLStorageAdapter',
    logic_adapter = [
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch',
        {
            'import_path':'chatterbot.logic.BestMatch',
            'maximum_similarity_threshold': 0.90
        }
    ],
    database_uri='sqlite:///database.sqlite3'
)

trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("data/data.yml")
