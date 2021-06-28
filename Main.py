import json
data = json.load(open("English.json"))

def defintion(word):
    if word in data:
        return data[word]
    else: 
        return ("This word was not found!")

word = input("select a word:")
print(defintion(word))