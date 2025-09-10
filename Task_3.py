def chatbot():
    print("Chatbot: Hi! Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("Chatbot: Hi!")
        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks!")
        elif user_input == "what is your name":
            print("Chatbot: I'm a simple Python chatbot!")
        elif user_input == "thanks":
            print("Chatbot: You're welcome!")
        elif user_input == "bye":
            print("Chatbot: Goodbye!")
            break
        else:
            print("Chatbot: I don't understand that.")

chatbot()
