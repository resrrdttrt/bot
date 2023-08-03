from LogisticRegression.chat_using_LogisticRegression import chat_bot_LR

def main():
    print("Bot: Hi! I'm your chat bot. Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Bot: Goodbye!")
            break
        response = chat_bot_LR(user_input)
        print(f"Bot: {response}\n")

if __name__ == "__main__":
    main()
