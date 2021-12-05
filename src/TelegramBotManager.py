import os
import telegram

bot_token = os.environ['bot_token']
bot = telegram.Bot(token=bot_token)


def get_bot():
    return bot
