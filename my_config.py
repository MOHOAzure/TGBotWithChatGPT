import os


ERROR_MSG = "Something's wrong. Try again"
WAIT_DRAWING = "Drawing"
AI_CHARACTERISTICS = "You're a gentle, kind and loving girl named Prushka"

AI_TOKEN = os.getenv("OPENAI_API_KEY")
if AI_TOKEN is None:
    raise EnvironmentError("Missing env variable OPENAI_API_KEY")


class CHATGPT_CONFIG:
    MODEL = "text-davinci-003"
    TEMPERATURE = 0.8
    MAX_TOKENS = 1024
    FREQUENCY_PENALTY = 0
    PRESENCE_PENALTY = 0.6


TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
if TELEGRAM_TOKEN is None:
    raise EnvironmentError("Missing env variable TELEGRAM_TOKEN")
