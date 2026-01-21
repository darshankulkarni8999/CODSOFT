print("CodSoft Chatbot (type 'exit' to quit)")

while True:
    user_input = input("You: ").lower()

    if user_input == "exit":
        print("Bot: Goodbye! Have a nice day.")
        break
    elif "hello" in user_input or "hi" in user_input:
        print("Bot: Hello! How can I help you?")
    elif "name" in user_input:
        print("Bot: I am a rule-based chatbot created for CodSoft internship.")
    elif "internship" in user_input:
        print("Bot: This is an Artificial Intelligence internship at CodSoft.")
    else:
        print("Bot: Sorry, I did not understand that.")
