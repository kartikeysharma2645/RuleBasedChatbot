while True:
    user_input = input("You: ").lower().strip().strip("!?")        # Normalize user input by converting it to lowercase and removing trailing punctuation.

    # Check predefined keywords and questions to determine the appropriate response.
    if user_input == "hello" or user_input == "hi" or user_input == "hey":
        print("Bot: Hello! How can I help you?")
    elif user_input == "what is your name":
        print("Bot: I am a rule-based chatbot.")
    elif user_input == "what can you do":
        print("Bot: I can answer questions using predefined rules.")
    elif user_input == "how are you":
        print("Bot: I'm doing great! How can I help you?")
    elif user_input == "what is python":
        print("Bot: Python is a high-level, general-purpose programming language.")
    elif user_input == "help":
        print("Bot: I can respond to greetings and a few predefined questions. Try asking what I can do.")
    elif user_input == "bye" or user_input == "goodbye":
        print("Bot: Goodbye!")
        break      # Exit the conversation loop.
    else:
        print("Bot: Sorry, I don't understand that.")
