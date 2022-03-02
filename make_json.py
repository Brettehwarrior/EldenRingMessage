import json
import string

templates = open('templates.txt', 'r').read().splitlines()
conjunctions = [s+'\n' if s in string.punctuation else '\n'+s for s in open('conjunctions.txt', 'r').read().splitlines()]
word_lines = open('words.txt', 'r').read().splitlines()
words = {}
curr_category = ''
for line in word_lines:
    if line.isupper():
        curr_category = line.lower()
        words[curr_category] = []
        continue
    if line != '':
        words[curr_category].append(line)

messages = {}
messages['templates'] = templates
messages['conjunctions'] = conjunctions
messages['words'] = words

print(messages)
with open('messages.json', 'w') as f:
    json.dump(messages, f, indent=4)