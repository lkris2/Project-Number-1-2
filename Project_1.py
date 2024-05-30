from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import random

# Create the main chatbot
bot = ChatBot("chatbot", read_only=False, 
              logic_adapters=[{"import_path": "chatterbot.logic.BestMatch",
                               "default_response": "Sorry, I don't understand what you mean by the response",
                               "maximum_similarity_threshold": 0.9}])

# Train the main chatbot
list_to_train = [
    "hi", "hi there",
    "what's your name?", "I'm a chatbot",
    "how are you", "I'm fine. How about you?",
    "I'm fine", "Nice. Can I do anything for you?",
    "how old are you?", "I'm ageless",
    "tell me a joke!", "Why was the math book sad?",
    "why", "Because it had too many problems.",
    "why are you so mad?", "I'm not!",
    "Do you have an iPhone?", "I've everything. Do you want to do a quiz?",
    "What's your favourite food?", "Nah, I don't eat!",
    "What's your job?", "I answer questions",
    "I don't know what you're talking about",
    "yes", "Great!",
    "no", "Oh, I see.",
    "yea", "Great!",
    "yeah", "Great!",
    "sure", "Great!"
]

list_to_train2 = [
    "hi", "hi there",
    "what's your name?", "I'm a chatbot",
    "how are you", "I'm fine. How about you?",
    "I'm fine", "Nice. Can I do anything for you?",
    "how old are you?", "I'm ageless",
    "tell me a joke!", "Why was the math book sad?",
    "why", "Because it had too many problems.",
    "why are you so mad?", "I'm not!",
    "Do you have an iPhone?", "I've everything. Do you want to do a quiz?",
    "What's your favourite food?", "Nah, I don't eat!",
    "What's your job?", "I answer questions",
    "I don't know what you're talking about",
    "yes", "Great!",
    "no", "Oh, I see.",
    "yea", "Great!",
    "yeah", "Great!",
    "sure", "Great!"
]

trainer = ListTrainer(bot)
trainer.train(list_to_train)

# Create the quiz chatbot
quiz_bot = ChatBot("QuizBot", logic_adapters=["chatterbot.logic.UnitConversion"])

# Control flow variable and state tracking
in_quiz_mode = False
last_question = None

# List of questions for the chatbot to ask
bot_questions = [
    "What's your favorite color?",
    "Do you like movies?",
    "What is your favorite hobby?",
    "Have you read any good books lately?",
    "What's your favorite type of music?"
]

# Function to determine if the bot should ask a question
def should_ask_question():
    return random.choice([True, False])

# Function to generate context-aware responses
def context_aware_response(user_input, last_question):
    responses = {
        "What's your favorite color?": f"{user_input.capitalize()} is a beautiful color!",
        "Do you like movies?": "Great! Movies are a wonderful way to relax.",
        "What is your favorite hobby?": f"{user_input.capitalize()} sounds like a fun hobby!",
        "Have you read any good books lately?": "That sounds interesting. I love a good book!",
        "What's your favorite type of music?": f"{user_input.capitalize()} is a great genre!"
    }
    return responses.get(last_question, "Interesting!")

while True:
    user_input = input("You: ").strip().lower()
    
    if in_quiz_mode:
        if user_input in ["quit", "exit", "stop"]:
            in_quiz_mode = False
            print("ChatBot: Exiting quiz mode.")
        else:
            response = quiz_bot.get_response(user_input)
            print("QuizBot: " + str(response))
    else:
        # Check for command to enter quiz mode
        if user_input in ["quiz time", "start quiz", "do a quiz"]:
            in_quiz_mode = True
            print("ChatBot: Entering quiz mode. You can ask questions on unit conversion or type 'quit' to exit quiz mode.")
        else:
            # Handling follow-up question about the joke
            if last_question == "tell me a joke!" and user_input in ["why", "why was it sad?", "explain"]:
                response = "Because it had too many problems."
            elif last_question in bot_questions:
                response = context_aware_response(user_input, last_question)
            else:
                response = bot.get_response(user_input)
            
            print("ChatBot: " + str(response))
            
            # Update the last question
            last_question = user_input

            # Check if the bot should ask a question, but avoid overlapping responses
            if should_ask_question() and last_question not in ["tell me a joke!", "why", "why was it sad?", "explain"]:
                bot_question = random.choice(bot_questions)
                print(f"ChatBot: {bot_question}")
                last_question = bot_question
        
        if "Do you want to do a quiz?" in str(response):
            if user_input in ["yes", "sure", "ok", "yeah"]:
                in_quiz_mode = True
                print("ChatBot: Entering quiz mode. You can ask questions on unit conversion or type 'quit' to exit quiz mode.")
