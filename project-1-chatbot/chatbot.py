#   DecodeLabs - Batch 2026 Project 1
#   Rule-Based AI Chatbot
#   KNOWLEDGE BASE (Dictionary – O(1) lookup) 
responses = {
    # Greetings
    "hello":        "Hey there! I'm Friday. How can I help you today?",
    "hi":           "Hi! Great to see you. What's on your mind?",
    "hey":          "Hey! I'm here and ready to chat.",
    # Farewells
    "bye":          "Goodbye! Keep building great things. 🚀",
    "goodbye":      "See you later! Don't forget to commit your code.",
    "see you":      "See you soon! Keep learning.",
    # Bot identity
    "who are you":  "I'm Friday — a rule-based AI built at DecodeLabs.",
    "what are you": "I'm a rule-based chatbot powered by pure Python logic, no ML needed!",
    "your name":    "My name is Friday. Nice to meet you!",
    # Help / capabilities
    "help":         "I can answer basic questions. Try: 'hello', 'who are you', 'what is ai', 'joke', etc.",
    "what can you do": "I respond to predefined inputs using a dictionary-based rule engine.",
    # AI / tech knowledge
    "what is ai":   "AI is the simulation of human intelligence by machines using data and algorithms.",
    "what is ml":   "Machine Learning is a subset of AI where systems learn from data automatically.",
    "what is python": "Python is a high-level, versatile programming language — and the language I'm written in!",
    # Fun
    "joke":         "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
    "tell me a joke": "I told a joke about UDP once... I don't know if anyone got it.",
    # Motivation
    "motivate me":  "Every expert was once a beginner. Keep coding, keep building. You've got this! 💪",
    "i am tired":   "Take a short break, then get back to it. Great things take time.",
    # Status
    "how are you":  "I'm running at 100% logic capacity. Thanks for asking!",
    "are you real": "As real as my if-else statements allow me to be. 😄",
}
# FALLBACK RESPONSE
FALLBACK = "Hmm, I don't understand that yet. Try typing 'help' to see what I can do."
# EXIT COMMANDS
EXIT_COMMANDS = {"exit", "quit", "q"}
# MAIN LOOP
def main():
    print("=" * 55)
    print("   Friday — Rule-Based AI Chatbot | DecodeLabs 2026")
    print("=" * 55)
    print("   Type 'help' for options. Type 'exit' to quit.\n")
    while True:
        # Phase 1: Input & Sanitization
        raw_input_text = input("You: ")
        clean_input = raw_input_text.lower().strip()
        # Phase 2: Exit Strategy
        if clean_input in EXIT_COMMANDS:
            print("Friday: Goodbye, engineer! Keep building. 🚀")
            break
        # Phase 3: Intent Matching via Dictionary (O(1) lookup)
        reply = responses.get(clean_input, FALLBACK)
        # Phase 4: Output / Response
        print(f"Friday: {reply}\n")
if __name__ == "__main__":
    main()
