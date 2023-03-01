from my_config import ERROR_MSG, AI_TOKEN, TELEGRAM_TOKEN, CHATGPT_CONFIG, AI_PROMPT_PREFIX, WAIT_DRAWING
from my_logger import logger
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import openai
openai.api_key = AI_TOKEN


def ai_say(prompt):
    try:
        response = openai.Completion.create(
            model=CHATGPT_CONFIG.MODEL,
            prompt=f"{AI_PROMPT_PREFIX}{prompt}",
            temperature=CHATGPT_CONFIG.TEMPERATURE,
            max_tokens=CHATGPT_CONFIG.MAX_TOKENS,
            top_p=1,
            frequency_penalty=CHATGPT_CONFIG.FREQUENCY_PENALTY,
            presence_penalty=CHATGPT_CONFIG.PRESENCE_PENALTY
        )
        return response['choices'][0]['text'].strip()
    except Exception as e:
        logger.error(f"ChatGPT fail: {str(e)}")
        return ERROR_MSG


def ai_draw(prompt):
    try:
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="512x512"#"1024x1024"
        )
        return response['data'][0]['url']
    except openai.error.OpenAIError as e:
        logger.error(e.http_status)
        logger.error(e.error)
        err_msg = f"Prompt: {prompt}. {ERROR_MSG}. {e.error.message}"
        logger.error(err_msg)
        return err_msg
    except Exception as e:
        logger.error(f"ChatGPT fail: {str(e)}")
        return ERROR_MSG
    
async def say(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.debug(context.args)
    prompt = ' '.join(context.args)
    response = ai_say(prompt)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

async def draw(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.debug(context.args)
    prompt = ' '.join(context.args)
        
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"{WAIT_DRAWING}: {prompt}")
    
    response = ai_draw(prompt)
    
    if response is None or ERROR_MSG in response:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=response)
    else:
        await context.bot.send_photo(chat_id=update.effective_chat.id, photo=response)

def start_bot():
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    say_handler = CommandHandler('s', say)
    draw_handler = CommandHandler('d', draw)
    application.add_handler(say_handler)
    application.add_handler(draw_handler)
    application.run_polling()


if __name__ == "__main__":
    logger.info('Start')
    start_bot()
    logger.info("End")
