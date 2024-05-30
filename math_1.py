from chatterbot import ChatBot

bot = ChatBot("Quiz",logic_adapters = ["chatterbot.logic.UnitConversion"])

while True:
    math_eq = input("Ask a question on unit conversion: ")
    cjat = str(bot.get_response(math_eq))
    print(cjat)