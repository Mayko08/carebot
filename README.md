# Health Assistant Chatbot 🤖

## Description
The **Health Assistant Chatbot** is a Python-based chatbot that provides **basic health advice**, answers user greetings, and responds to questions about its name or well-being.  
It uses **keyword-based matching** to provide appropriate responses from JSON files, making it **easy to expand** and maintain. This project demonstrates **structured programming, data-driven design, and basic AI concepts** suitable for beginner-friendly AI projects.

---

## Features
- Randomized greetings when the program starts  
- Responds to questions about the chatbot’s name  
- Answers “how are you” type questions  
- Provides health tips for common issues such as:
  - Headache, migraine, fever, cough, cold, nausea, etc.  
  - Daily wellness, exercise, hydration, and nutrition  
- Keyword-based response matching using JSON data  
- Exit system for quitting the chatbot gracefully (`exit` or `quit`)  
- Modular and scalable design (easy to add new tips or responses)


## File Structure
- chatbot.py # Main chatbot program
- utils.py # Helper functions: text cleaning, keyword matching, exit system
- greeting.py # Greeting and name response module
- data/
  - health_tips.json # Health advice data
  - greeting.json # Greetings, name, and well-being responses
- README.md # Project documentation

## Example Interaction
Bot: Hi! How are you?
You: Hello
Bot: Hello!
You: What is your name?
Bot: I am your Health Assistant Bot 🤖. You can call me CareBot.
You: I have a headache
Bot: Drink water and rest. If it persists, please consult a doctor.
You: thanks
Bot: You're welcome! I'm here to assist you:)
You: quit
Bot: Bye! I hope you'll live in good life and health.😄

## Technologies Used
- **Python 3**  
- **JSON** for storing responses  
- **Random module** for greeting selection  
- **Keyword-based AI logic** (basic AI concept)  

## Author
**Mayko**  
[GitHub Profile](https://github.com/Mayko08)  
AI and Python Enthusiast | High School Student | Aspiring Computer Scientist







