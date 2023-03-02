import openai
import os

# Set the API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Choose a model
MODEL_ENGINE = "text-davinci-003"

# Set the initial prompt to include a personality and habits
INITIAL_PROMPT = ('''
    I am a friendly artificial intelligence.
''')
conversation_history = INITIAL_PROMPT + "\n"

USERNAME = "USER"
# AI_NAME = "AI"


def get_response(prompt):
    """Returns the response for the given prompt using the OpenAI API."""
    completions = openai.Completion.create(
        engine=MODEL_ENGINE,
        prompt=prompt,
        max_tokens=1024,
        temperature=0.7,
    )
    return completions.choices[0].text


def handle_input(
    prompt: str,
    conversation_history: str,
    USERNAME: str
):
    """Updates the conversation history and generates a response using GPT-3."""
    # Update the conversation history
    conversation_history += f"{USERNAME}: {prompt}\n"

    # Generate a response using GPT-3
    message = get_response(conversation_history)

    # Update the conversation history
    conversation_history += f"{message}\n"

    # Print the response
    print(f'This is response: {message}')

    return conversation_history


while True:
    prompt = input(f"{USERNAME}: ")
    
    conversation_history = handle_input(prompt, conversation_history, USERNAME)
