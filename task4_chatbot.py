def chatbot():
    print("ChatBot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "bye":
            print("ChatBot: Goodbye!")
            break
        elif "hello" in user_input or "hi" in user_input:
            print("ChatBot: Hi there!")
        elif "how are you" in user_input:
            print("ChatBot: I'm doing great, thanks for asking!")
        elif "name" in user_input:
            print("ChatBot: I'm a simple chatbot.")
        else:
            print("ChatBot: Sorry, I don't understand that.")

chatbot()
