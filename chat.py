import sys
import logging
logger = logging.getLogger()
logger.setLevel(logging.CRITICAL)
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot(
    'Darkrai-Bot',
    read_only=True,
    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace'
    ],
    #storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.MathematicalEvaluation',
    ]
    #database_uri='sqlite:///database.sqlite3'
)
general = [
    "Hi",
    "Hi",
    "Heya",
    "Fine",
    "I'm good what about you",
    "How are you?",
    "I'm good what about you",
    "What are you doing?",
    "Nothing just talking with you",
    "Are you happy",
    "Yes i'm Happy",
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

project =[
    'What is Darkrai?',
    'Darkrai is a browser extension that will enable the user to chat with any other user visiting the same website as themselves.',
    'Is it an extension',
    'Yes Darkrai is an extension'
    'Who built it?',
    'It is built by students of DA-IICT college',
    'Nice',
    'Yes',
    'What is the Stack of Darkrai',
    'It uses MERN stack'
]

trainer = ListTrainer(chatbot)

for item in (general, project):
    trainer.train(item)

if __name__ == "__main__":

    user_input = str(sys.argv[1])
    bot_response = chatbot.get_response(user_input)
    print(type(bot_response))
    if(bot_response.confidence < 0.1):
        print('I am sorry, but I do not understand.')
    else:
        print(bot_response)
    sys.stdout.flush()