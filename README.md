# personal-ai-project
# 🧠 Personal AI Project – Local Chatbot using TinyLlama

This is a simple command-line AI chatbot powered by a local LLM (TinyLlama via [Ollama](https://ollama.com)). It allows you to chat with an AI assistant offline — no internet or paid API key required.

## 🚀 Features

- Conversational chat loop in terminal
- Works fully offline with open-source models (no OpenAI API needed)
- Gracefully handles network errors and unexpected responses
- Easily extensible to support other models (e.g., LLaMA3, Mistral)

## 🧰 Tech Stack

- Python
- [Ollama](https://ollama.com)
- `requests` package

## 🧪 Demo

```bash
$ python ai_chat.py
Start chatting with TinyLlama (type 'exit' to quit)
You: hello
AI: Hello! How can I help you today?
