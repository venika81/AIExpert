from textblob import TextBlob
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    return polarity

def sentiment_response(polarity):
    if polarity > 0.3:
        return Fore.GREEN + "That's a positive vibe! 😊"
    elif polarity < -0.3:
        return Fore.RED + "Oh no! That sounds negative. 😟"
    else:
        return Fore.YELLOW + "Sounds neutral. 😐"

def sentiment_spy():
    print(Fore.CYAN + Style.BRIGHT + "👁️ Welcome to Sentiment Spy!")
    print(Fore.MAGENTA + "Type something and I'll spy on the sentiment. Type 'exit' to quit.\n")

    while True:
        user_input = input(Fore.WHITE + "You: ")

        if user_input.lower() in ['exit', 'quit']:
            print(Fore.CYAN + "👋 Sentiment Spy signing off. Stay emotionally aware!")
            break

        polarity = analyze_sentiment(user_input)
        response = sentiment_response(polarity)

        print(response + f" (Polarity Score: {polarity:.2f})\n")

# Run the chatbot
if __name__ == "__main__":
    sentiment_spy()
