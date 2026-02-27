#!/usr/bin/env python3
"""
Task 3: Initialize Chat with Ollama
Learn how to set up and use local Ollama models with LangChain.

Learning Goal: Chat with local LLMs without cloud APIs.
Ollama version: 0.1.37
"""

import os
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, AIMessage

def initialize_ollama():
    """
    Initialize Ollama with LangChain.
    
    Prerequisites:
    1. Ollama must be installed and running
    2. A model must be pulled (e.g., ollama pull llama2)
    3. Ollama API runs on http://localhost:11434 by default
    """
    
    # Initialize Ollama model
    # Default model options: "llama3", "llama2", "mistral", "neural-chat", etc.
    # Check available models with: ollama list
    
    ollama = ChatOllama(
        model="llama3",  # Change to your preferred model
        base_url="http://localhost:11434",  # Default Ollama port
        temperature=0.7,  # Controls randomness (0-1, lower = more deterministic)
    )
    
    return ollama

def chat_with_ollama(ollama, user_message: str) -> str:
    """
    Send a message to Ollama and get a response.
    
    Args:
        ollama: ChatOllama instance
        user_message: The message to send
    
    Returns:
        The AI's response as a string
    """
    
    # Create a message and invoke the model
    message = HumanMessage(content=user_message)
    response = ollama.invoke([message])
    
    # Extract the text content from the response
    return response.content

def main():
    print("🤖 Task 3: Chat with Ollama")
    print("=" * 60)
    
    print("\n📋 Prerequisites:")
    print("   1. Ollama installed and running")
    print("   2. A model pulled (e.g., ollama pull llama2)")
    print("   3. Ollama listening on http://localhost:11434")
    
    print("\n⚙️  Initializing Ollama...")
    
    try:
        ollama = initialize_ollama()
        print("✅ Ollama initialized successfully!")
    except Exception as e:
        print(f"❌ Failed to initialize Ollama: {e}")
        print("\n💡 Troubleshooting:")
        print("   - Is Ollama running? Try: ollama serve")
        print("   - Check available models: ollama list")
        print("   - Pull a model if needed: ollama pull llama2")
        return
    
    # Interactive chat loop
    print("\n" + "=" * 60)
    print("💬 Chat with Ollama (type 'quit' to exit)")
    print("=" * 60)
    
    while True:
        try:
            user_input = input("\n🧑 You: ").strip()
            
            if user_input.lower() == "quit":
                print("\n👋 Goodbye!")
                break
            
            if not user_input:
                print("⚠️  Please enter a message.")
                continue
            
            print("\n🤖 Ollama: ", end="", flush=True)
            response = chat_with_ollama(ollama, user_input)
            print(response)
            
        except KeyboardInterrupt:
            print("\n\n👋 Chat interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")
            print("💡 Make sure Ollama is still running on http://localhost:11434")

def demo_chat():
    """
    Run a simple demo without interactive input.
    Useful for testing/scripting.
    """
    print("\n🎬 Running Demo Chat...")
    print("=" * 60)
    
    try:
        ollama = initialize_ollama()
        
        test_prompts = [
            "What is machine learning in one sentence?",
            "Explain Python's list comprehension briefly.",
            "Name three benefits of using APIs."
        ]
        
        for prompt in test_prompts:
            print(f"\n📝 Prompt: {prompt}")
            response = chat_with_ollama(ollama, prompt)
            print(f"🤖 Response: {response}\n")
            print("-" * 60)
        
        print("\n✅ Demo completed!")
        
    except Exception as e:
        print(f"❌ Demo failed: {e}")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--demo":
        demo_chat()
    else:
        main()
