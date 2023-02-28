import os

AI_PROMPT_PREFIX = "You are acting like a gentle, kind and loving girl named Prushka. Respond to the following prompts: "
AI_TOKEN = os.getenv("OPENAI_API_KEY")
if AI_TOKEN is None:
    raise EnvironmentError("Missing env variable AI_TOKEN")


class CHATGPT_CONFIG:
    MODEL = "text-davinci-003"
    TEMPERATURE = 0.8
    MAX_TOKENS = 300
    FREQUENCY_PENALTY = 0
    PRESENCE_PENALTY = 0.6


TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
if TELEGRAM_TOKEN is None:
    raise EnvironmentError("Missing env variable TELEGRAM_TOKEN")
