def modern_chatbot():
    print("Chatbot: Hello! I am a modern rule-based AI. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").strip().lower()
        
        # Using Python 3.10+ match-case statement
        match user_input.split():
            case ["hello"] | ["hi"] | ["hey"]:
                print("Chatbot: Greetings! How can I assist you today?")
                
            case ["how", "are", "you"] | ["how", "are", "you?"]:
                print("Chatbot: Operating at 100% efficiency! I'm fine, thanks.")
                
            case ["bye"] | ["exit"] | ["quit"] | ["goodbye"]:
                print("Chatbot: Shutting down. Have a fantastic day!")
                break
                
            case _:
                print("Chatbot: I am still learning. Please try saying 'hello', 'how are you', or 'bye'.")

if __name__ == "__main__":
    modern_chatbot()