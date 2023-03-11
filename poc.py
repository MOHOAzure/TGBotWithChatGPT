from revChatGPT.V1 import Chatbot
import os

chatbot = Chatbot(
    config={
        "access_token": f"{os.getenv('ChatGPT_TOKEN')}"
    }, conversation_id=f"{os.getenv('conv_id')}"
)


def ask_chatgpt(chatbot, prompt):
    response = ""

    for data in chatbot.ask(
        prompt
    ):
        response = data["message"]
    return response


query = "Hello?"

response = ask_chatgpt(chatbot, query)
# response = chatbot.get_conversations()

print(response)
