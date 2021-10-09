from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

chatbot = ChatBot('CoronaBot');

##conversation = ["Hello","Hi there","How are doing?","Thank you"]

trainingfileDS = open('trainingData/train_coronaDS.txt').read().splitlines()
trainingData = trainingfileDS

trainer = ListTrainer(chatbot)

trainer.train(trainingData)