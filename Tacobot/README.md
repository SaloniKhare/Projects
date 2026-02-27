# 🤖 TacoBot

**TacoBot – AI-Based Restaurant Chatbot using PyTorch**

TacoBot is an intelligent conversational chatbot built using Python and PyTorch.  
It is designed to simulate restaurant interactions such as table reservations, cancellations, and menu-related queries through natural language processing.

This project focuses purely on backend AI logic and runs in the terminal (console-based application).

---

## 🚀 Project Overview

TacoBot uses:
- Natural Language Processing (NLP)
- A Neural Network built with PyTorch
- Intent classification
- Pattern-based conversational design

The chatbot predicts user intent based on trained data and responds accordingly.

---

## 🧠 Features

✔ Intent classification using neural networks  
✔ Handles restaurant-related tasks:
- Table reservation
- Reservation cancellation
- Menu inquiries
- Order total calculation  
✔ Trained model stored in `.pth` file  
✔ Modular and structured Python code  

---

## 🗂 Project Structure
Tacobot/
│
├── chat.py # Main chatbot execution file
├── model.py # Neural network model architecture
├── nltk_utils.py # NLP preprocessing utilities
├── intents.json # Training data (intents and patterns)
├── data.pth # Saved trained model
├── database.py # Reservation database handling
├── orders.py # Menu & order logic
├── requirements.txt # Dependencies
└── README.md

---

## ⚙️ How It Works
1. User enters a message in the terminal.
2. Text is tokenized and processed using NLP utilities.
3. The neural network predicts the intent.
4. Based on predicted intent:
   - The bot performs an action (reserve/cancel/order).
   - Or returns a predefined response.
5. Output is displayed in the console.
