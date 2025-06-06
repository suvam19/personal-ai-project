import requests

def chat_withai(model="tinyllama"):
    print("Start chatting with TinyLlama (type 'exit' to quit)")
    while True:
        prompt = input("You: ")
        if prompt.lower() in ["exit", "quit"]:
            break
        try:
    
            response = requests.post("http://localhost:11434/api/generate", json = {
                "model": model,
                "prompt": prompt,
                "stream": False
            })
            data = response.json()
            print("AI:", data["response"])
        except KeyError:
                print("⚠️ Unexpected response format:", data)
        except requests.exceptions.ConnectionError:
                print("❌ Unable to connect to Ollama. Is it running?")
                break

chat_withai()