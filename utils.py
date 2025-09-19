import string
import sys

def clean_text(text):
    """
    Lower case and remove punctuation.
    """

    text = text.lower()
    text = text.translate(str.maketrans('','',string.punctuation)).strip()

    return text


def find_response(user_input, responses):
    """
    Find the best response for the user_input based on keywords in responses dictionary.
    If no keyword matches, return the default response.
    """
    text = clean_text(user_input)

    matched_keywords = []

    for keyword in responses:
        if keyword != "default" and keyword in text:
            matched_keywords.append(responses[keyword])

    if matched_keywords:
        return " ".join(matched_keywords)
    
    if text in ("exit", "quit"):
        exit_sys(user_input)

    return responses["default"]
        
def exit_sys(user_input):
    """
    Exit the program if the user types in 'exit' or 'quit'.
    """

    if user_input.lower() in ('exit', 'quit'):
        print("Bye! I hope you'll live in good life and health.😄")
        sys.exit()

def split_words(user_input):
    """
    Spliting the words from the text to find the keywords.
    """
    text = user_input.split()
    return text

    
            

