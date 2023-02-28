from my_config import AI_TOKEN, TELEGRAM_TOKEN, CHATGPT_CONFIG
from my_logger import logger
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import openai
openai.api_key = AI_TOKEN


def ai_response(prompt):
    try:
        response = openai.Completion.create(
            model=CHATGPT_CONFIG.MODEL,
            prompt=prompt,
            temperature=CHATGPT_CONFIG.TEMPERATURE,
            max_tokens=CHATGPT_CONFIG.MAX_TOKENS,
            top_p=1,
            frequency_penalty=CHATGPT_CONFIG.FREQUENCY_PENALTY,
            presence_penalty=CHATGPT_CONFIG.PRESENCE_PENALTY
        )
        return response['choices'][0]['text'].strip()
    except Exception as e:
        logger.error(f"ChatGPT fail: {str(e)}")
        return "Something's wrong. Try again"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.debug(context.args)
    prompt = ' '.join(context.args)
    response = ai_response(prompt)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)


def start_bot():
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    start_handler = CommandHandler('s', start)
    application.add_handler(start_handler)
    application.run_polling()


if __name__ == "__main__":
    logger.info('Start')
    start_bot()
    logger.info("End")
