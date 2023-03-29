import openai
import os
openai.api_key = os.getenv("OPENAI_API_KEY")
MODEL_ENGINE = "gpt-4"  # Or "gpt-3.5-turbo"
USERNAME = "USER"


def get_response(prompt):
    """Returns the response for the given prompt using the OpenAI API."""
    response = openai.ChatCompletion.create(
        model=MODEL_ENGINE,
        temperature=1.2,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant. Always say ❤️ with response"
            },
            {
                "role": "user",
                "content": prompt
            },
            # {
            #     "role": "assistant",
            #     "content": ""
            # },
            # {
            #     "role": "user",
            #     "content": "Next prompt"
            # }
        ]
    )
    # print(f"response: {response}")
    return response.choices[0].message.content


def save_available_models():
    with open("available_models.txt", "w") as my_file:
        my_file.write(str(openai.Model.list()))

# save_available_models()


while True:
    prompt = input(f"{USERNAME}: ")
    message = get_response(prompt)
    print(f"message: {message}")
