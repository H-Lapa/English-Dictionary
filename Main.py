import json
from difflib import get_close_matches
data = json.load(open("English.json"))

def defintion(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        choice = input("Did you mean %s?" % get_close_matches(word, data.keys())[0] )
        choice = choice.lower()
        if choice == "y":
            return data[get_close_matches(word, data.keys())[0]]
        else:
            return ("This word was not found!")
    else: 
        return ("This word was not found!")

word = input("select a word:")
print(defintion(word))