import random
import json
import database as db
import torch
import orders as o
from model import NeuralNet
from nltk_utils import bag_of_words, tokenize


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "data.pth"
data = torch.load(FILE,weights_only=True)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "TacoBot🌮"
print("-------------------------------------------------")
print("🌮🌮Chat with TacoBot!🌮🌮(type 'quit' to exit)")
print("-------------------------------------------------")
while True:
    # sentence = "do you use credit cards?"
    sentence = input("You👨: ")
    if sentence.lower() == "quit" or sentence.lower() == "exit" :
        break

    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                if tag == "reserve_table":
                    print(f"{bot_name}: {random.choice(intent['responses'])}")
                    name = input('You👨: ')
                    print(f"{bot_name}:Can I have your phone number?")
                    phone = input('You👨: ')
                    print(f"{bot_name}:Got it! When would you like the reservation (date and time)?(dd/mm/yy hh:mm)")
                    date_time = input('You👨: ')
                    print(f"{bot_name}:",db.check_and_book_table(name, phone, date_time))
                elif tag == "cancel_reservation":
                    print(f"{bot_name}: {random.choice(intent['responses'])}")
                    phone = input('You👨: ')
                    print(f"{bot_name}:",db.cancel_reservation(phone))
                elif tag == "menu_request":
                    print(f"{bot_name}: {random.choice(intent['responses'])}")
                    print(f"{bot_name}:Your Total payable amount is {o.order()}$\nAnything else that I can do for you?")
                else:
                    print(f"{bot_name}: {random.choice(intent['responses'])}")
    else:
        print(f"{bot_name}: I do not understand...")
