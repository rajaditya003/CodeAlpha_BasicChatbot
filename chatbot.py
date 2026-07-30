# =============================================================================
# Project: Basic Chatbot
# Internship: CodeAlpha Python Internship
# Author: Aashu Raj
# =============================================================================

import random


def show_banner():
    """
    Displays a friendly welcome banner when the chatbot starts.
    """
    print("=" * 50)
    print("           🤖 WELCOME TO BASIC CHATBOT 🤖")
    print("=" * 50)
    print("Type 'bye', 'exit', or 'quit' to end the chat.")
    print("-" * 50)


def get_response(user_input):
    """
    Analyzes the user's input and returns an appropriate predefined response.
    Uses string methods and an if-elif block for decision making.
    
    Args:
        user_input (str): The cleaned and lowercased input from the user.
        
    Returns:
        str: The chatbot's reply.
    """
    # Check for greetings
    if user_input in ["hello", "hi", "hey"]:
        # Pick a random friendly greeting
        responses = [
            "Hello! Nice to meet you.",
            "Hi! How can I help you today?"
        ]
        return random.choice(responses)

    # Check for common conversation questions
    elif user_input == "how are you":
        return "I'm just a computer program, but I'm feeling fantastic! How are you?"
        
    elif user_input == "what is your name":
        return "I am Basic Chatbot, your friendly virtual assistant."
        
    elif user_input == "who created you":
        return "I was created by Aashu Raj for the CodeAlpha Python Internship."
        
    elif user_input in ["thank you", "thanks"]:
        return "You're very welcome! I'm happy to help."
        
    elif user_input == "good morning":
        return "Good morning! I hope you have a wonderful day ahead."
        
    elif user_input == "good afternoon":
        return "Good afternoon! Hope your day is going well."
        
    elif user_input == "good evening":
        return "Good evening! It's nice to chat with you."
        
    elif user_input == "help":
        return "I can answer simple questions like 'how are you', 'what is your name', and more. Try saying hello!"
        
    # Catch-all for unknown input
    else:
        return "Sorry, I don't understand that yet."


def goodbye():
    """
    Displays the farewell message when the user exits the chat.
    """
    print("-" * 50)
    print("🤖 Chatbot: Thank you for chatting. Have a wonderful day!")
    print("=" * 50)


def chat():
    """
    The main chat loop that continually interacts with the user.
    Handles input validation and triggers the appropriate responses.
    """
    # Start by showing the welcome banner
    show_banner()
    
    # Enter an infinite loop to keep the chat going
    while True:
        # Prompt the user for input
        raw_input = input("\nYou: ")
        
        # Clean the input: remove extra spaces from start/end and convert to lowercase
        # This handles extra spaces and mixed uppercase/lowercase characters
        clean_input = raw_input.strip().lower()
        
        # Validate for empty input
        if clean_input == "":
            print("🤖 Chatbot: Please say something! I'm listening.")
            continue  # Skip to the next iteration of the loop
            
        # Check if the user wants to exit
        if clean_input in ["bye", "exit", "quit"]:
            goodbye()
            break  # Exit the while loop
            
        # If not exiting, get the chatbot's response
        response = get_response(clean_input)
        
        # Print the response
        print(f"🤖 Chatbot: {response}")


# =============================================================================
# Entry Point
# =============================================================================
if __name__ == "__main__":
    chat()
