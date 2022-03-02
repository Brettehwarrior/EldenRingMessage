import json
import random

class MessageFactory:
    def __init__(self, messages):
        self.messages = messages

    def word(self):
        category, words = random.choice(list(self.messages['words'].items()))
        return random.choice(words)

    def template(self):
        template_text = random.choice(self.messages['templates'])
        word_text = self.word()
        return template_text.replace('****', word_text)

    def conjunction(self):
        return random.choice(self.messages['conjunctions'])

    def message(self):
        layouts = [
            'T',
            'TCT'
        ]
        layout = random.choice(layouts)
        message_text = ''
        for s in layout:
            if s == 'T':
                message_text += self.template()
            elif s == 'C':
                message_text += self.conjunction() + ' '

        return message_text


if __name__ == '__main__':
    with open('messages.json', 'r') as file:
        messages = json.load(file)
        factory = MessageFactory(messages)

        for i in range(10):
            print(factory.message() + '\n')

