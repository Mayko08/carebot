import random
import json

"""
Load the data
"""
with open("data/greeting.json", "r") as file:
    data = json.load(file)

def greet_user():
    """
    Greeting to user
    """
    greetings = data["greetings"]
    return random.choice(greetings)

def answer_user(name):
    """
    Answer the user when they ask the name, well being, or say 'Hi' simply. 
    """
    text = name.lower()
    
    if "your name" in text or "who are you" in text:
       return random.choice(data["name_responses"])
    elif "hi" in text or "hello" in text or "nice to meet you" in text:
        return random.choice(data["responses"])
    elif "how are you" in text:
        return random.choice(data["wellbeing_responses"])

    
     
    
