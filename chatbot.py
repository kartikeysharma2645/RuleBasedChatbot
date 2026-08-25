while True:
    user_input = input("You: ").lower().strip().strip("!?")        # Normalize user input by converting it to lowercase and removing trailing punctuation.

    # Check predefined keywords and questions to determine the appropriate response.
    
    # 1. Exit commands
    if "bye" in user_input or "see you" in user_input:
        print("Bot: Goodbye!")
        break

    # 2. Greetings
    elif user_input == "hello" or user_input == "hi" or user_input == "hey":
        print("Bot: Hello! How can I help you?")

    # 3. Specific commands/questions
    elif user_input == "what is your name":
        print("Bot: I am a rule-based chatbot.")
    elif user_input == "help":
        print("Bot: I can respond to greetings and a few predefined questions. Try asking what I can do.")

    # 4. Phrase-based rules
    elif "what can you" in user_input:
        print("Bot: I can answer questions using predefined rules.")
    elif "how are you" in user_input:
        print("Bot: I'm doing great! How can I help you?")

    # 5. Knowledge/keyword rules
    elif "python" in user_input:
        print("Bot: Python is a high-level, general-purpose programming language.")
    elif "thank" in user_input:
        print("Bot: You're welcome!")

    # 6. Fallback
    else:
        print("Bot: Sorry, I don't understand that.")