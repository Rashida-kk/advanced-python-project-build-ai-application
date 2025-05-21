from textblob import TextBlob
# Define intents and their corresponding responses based on keywords
intents = {
    "houres":{
        "keywords":["hours","open","close"],
        "response":"we are open from 9 AM to 5 PM, Monday to Friday."
    },
    "return":{
        "keywords":["refund", "money back", "return"],
        "response":"I'd be happy to help you with the return process. Let me transfer you to a live agent."
    }
}
def get_response(message):
    #convert the message to lowercase for consistent keyword matching
    message = message.lower()
    #Check if the message contains any keywords associate with defined intents
    for intent_name, intent_data in intents.items():
        if any(word in message for word in intent_data["keywords"]):
            # Return the corresponding response if a keyword matches
            return intent_data["response"]
    # Analyze the sentiment of the message using TextBolb
        sentiment = TextBlob(message).sentiment.polarity

    #Return a response based on the sentiment score
    return(
      "That's so great to hear!" if sentiment > 0 else
           "I'm so sorry to hear that how can i help?" if sentiment < 0 else
           "I see, Can you tell me more about that?"
    )    

def chat():
     #Great the user and prompt for input
    print("chatbot: Hi, How can i help you today?")
    #Continuously prompt the user for input untill they choose to exit
    while (user_mesage := input("You: ").strip().lower())not in ["exit", "quit", "bye"]:
         print(f"\ChatBot: {get_response(user_mesage)}")

    #Thank the user for chatting when they exit 
    print("ChatBot: Thank you for chatting. Have a great day!")

if __name__ == "__main__":
     chat() # Start the chat when the script is executed      

