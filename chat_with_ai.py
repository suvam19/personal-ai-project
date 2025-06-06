import requests # For making HTTP requests to the local Ollama API

# Define a function to handle the chatbot interaction

def chat_withai(model="tinyllama"):

    # Intro message to user
    print("Start chatting with TinyLlama (type 'exit' to quit)")

    # Infinite loop to keep the conversation going until user types 'exit' or 'quit'
    while True:
        prompt = input("You: ")
        if prompt.lower() in ["exit", "quit"]:
            break
        try:
            # Make a POST request to the local Ollama API with the user's prompt
            response = requests.post("http://localhost:11434/api/generate", json = {
                "model": model, # Model to use (e.g., tinyllama)
                "prompt": prompt, # The user's message
                "stream": False # Set to False for full response in one go
            })
            data = response.json()
            print("AI:", data["response"])
        # Handle unexpected response structure from the API
        except KeyError:
                print("⚠️ Unexpected response format:", data)
        # Handle case where Ollama isn't running or cannot be reached
        except requests.exceptions.ConnectionError:
                print("❌ Unable to connect to Ollama. Is it running?")
                break
# Call the function to start the chat when the script runs
chat_withai()