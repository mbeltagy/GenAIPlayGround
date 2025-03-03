import os
from dotenv import load_dotenv
import openai

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

def chat_completion(prompt, model="gpt-3.5-turbo", max_tokens=150):
    try:
        # Create a completion request
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=max_tokens
        )

        # Extract the generated text from the response
        generated_text = response['choices'][0]['message']['content']
        return generated_text

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    user_prompt = "Hello, how are you?"
    completion = chat_completion(user_prompt)
    if completion:
        print("Generated Response:", completion)