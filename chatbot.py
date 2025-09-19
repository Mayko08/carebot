from utils import find_response, exit_sys
from greeting import greet_user, answer_user
import json
 
def main():
    """
    Load the file
    """
    with open("data/health_tips.json", "r") as file:
        data = json.load(file)

    
    """
    Instruction
    """
    print("To quit, you have to type 'exit' or 'quit'.")
    print()

    """
    Greet the user
    """
    greet = greet_user()
    print("Bot: ",greet)

    """
    Loop for user input
    """
    while True:
        user = input("You: ") 

        if user:
            answer = answer_user(user)
            if answer:
                print("Bot:", answer)
            else:
                print("Bot:", find_response(user, data))

        else:
            print("Bot: I'm sorry. I can't provide any advices without telling me.")
        print()

        if exit_sys(user):
            break
    
 

if __name__ == "__main__":
    main()



