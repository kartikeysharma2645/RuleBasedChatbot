user_input = input("You: ").lower()

if user_input == "hello" or user_input == "hi":
    print("Bot: Hello! How can I help you?")
elif user_input == "what is your name" or user_input == "what is your name?":
    print("Bot: I am a rule-based chatbot.")
elif user_input == "what can you do" or user_input == "what can you do?":
    print("Bot: I can answer questions using predefined rules.")
else:
    print("Bot: Sorry, I don't understand that.")feat: implement initial chatbot response rules