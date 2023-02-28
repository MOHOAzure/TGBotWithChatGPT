import os

# tg bot token
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

# Check the token is set
if TELEGRAM_TOKEN is None:
    raise EnvironmentError("Missing env variable TELEGRAM_TOKEN")

# chat rooms in telegram that bot would response
VALID_CHAT_ID = []
VALID_CHAT_ID.append(os.getenv('CHAT_ID_GROUP_MAIN'))
VALID_CHAT_ID.append(os.getenv('CHAT_ID_GROUP_TEST'))
VALID_CHAT_ID.append(os.getenv('CHAT_ID_DM'))
if len(VALID_CHAT_ID) == 0 or VALID_CHAT_ID is None:
    raise EnvironmentError("Missing env variable Chat ID")
