while True:
    user_input = input("You: ").lower().strip().strip("!?")

    # Check predefined keywords and questions to determine the appropriate response.

    # 1. Exit commands
    if "bye" in user_input or "see you" in user_input:
        print("Bot: Goodbye!")
        break

    # 2. Greetings
    elif user_input in ("hello", "hi", "hey"):
        print("Bot: Hello! How can I help you?")

    # 3. Specific questions and commands
    elif user_input == "what is your name":
        print("Bot: I am a rule-based chatbot.")

    elif user_input == "help":
        print("Bot: I can respond to greetings and a few predefined questions. Try asking what I can do.")

    # 4. Phrase-based rules
    elif "what can you" in user_input:
        print("Bot: I can answer questions using predefined rules.")

    elif "how are you" in user_input:
        print("Bot: I'm doing great! How can I help you?")

    elif "who created you" in user_input or "who made you" in user_input:
        print("Bot: I was created as a rule-based chatbot for an Artificial Intelligence internship project.")

    elif "what is your purpose" in user_input or "why were you created" in user_input:
        print("Bot: My purpose is to demonstrate how a chatbot can respond using predefined rules and keywords.")

    # 5. Time-related question
    elif "what time is it" in user_input:
        print("Bot: I don't have access to the current time, but you can check your system clock.")

    # 6. Knowledge-based keyword rules
    elif "python" in user_input:
        print("Bot: Python is a high-level, general-purpose programming language.")

    elif "artificial intelligence" in user_input or "what is ai" in user_input:
        print("Bot: Artificial Intelligence is the field of creating systems that can perform tasks that normally require human intelligence.")

    elif "machine learning" in user_input:
        print("Bot: Machine Learning is a branch of AI that allows computers to learn patterns from data and make predictions or decisions.")

    # 7. Conversational responses
    elif "thank" in user_input:
        print("Bot: You're welcome!")

    elif "joke" in user_input:
        print("Bot: Why do programmers prefer dark mode? Because light attracts bugs!")


    # 8. Fallback response
    else:
        print("Bot: Sorry, I don't understand that.")