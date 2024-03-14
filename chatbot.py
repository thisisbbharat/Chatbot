import random

class Chatbot:
    def __init__(self, name):
        self.name = name

    def greet(self):
        greetings = [
            "Hello, I'm {}! How can I assist you today?".format(self.name),
            "Hi there! What can I do for you today?",
            "Hey! I'm {}. How may I help you?".format(self.name)
        ]
        return random.choice(greetings)

    def respond(self, message):
        responses = {
            "how are you": "I'm just a program, so I don't have feelings, but thanks for asking!",
            "what's your name": "I'm {}.".format(self.name),
            "default": "I'm sorry, I don't understand. Can you please rephrase?"
        }
        return responses.get(message.lower(), responses['default'])

# Main program
if __name__ == "__main__":
    bot = Chatbot("ChatGPT")
    print(bot.greet())
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Bot: Goodbye!")
            break
        else:
            print("Bot:", bot.respond(user_input))
