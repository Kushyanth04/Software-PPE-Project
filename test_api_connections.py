import os
from openai import OpenAI
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

def test_apis():
    # Get API keys from environment variables
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')

    # Test OpenAI/ChatGPT connection
    try:
        print("\nTesting ChatGPT connection...")
        client = OpenAI(api_key=OPENAI_API_KEY)
        response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[{
                "role": "system",
                "content": "You are GPT-4 Turbo. Respond with only your model name."
            },
            {
                "role": "user",
                "content": "What model are you?"
            }],
            max_tokens=1000
        )
        print("SUCCESS: ChatGPT connection successful!")  
        print(f"Model response: {response.choices[0].message.content}")
        print(f"Actual model: {response.model}")
    except Exception as e:
        print("FAILED: ChatGPT connection failed!")
        print(f"Error: {str(e)}")

    # Test Claude connection
    try:
        print("\nTesting Claude connection...")
        anthropic = Anthropic(api_key=ANTHROPIC_API_KEY)
        message = anthropic.messages.create(
            model="claude-3-sonnet-20240229",
            max_tokens=1000,
            messages=[{
                "role": "user",
                "content": "Please identify yourself. Are you Claude? What version?"
            }]
        )
        print("SUCCESS: Claude connection successful!")
        print(f"Model response: {message.content}")
        print(f"Actual model: {message.model}")
    except Exception as e:
        print("FAILED: Claude connection failed!")
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    test_apis()
