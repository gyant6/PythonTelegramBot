import os
import telegram
import src.Sender as Sender
from src.Constants import commands
from src.TelegramBotManager import get_bot
from flask import Flask, request

# activate local env
# source venv/bin/activate
bot_token = os.environ['bot_token']
bot = get_bot()
app = Flask(__name__)
URL = os.environ['URL']


@app.route('/{}'.format(bot_token), methods=['POST'])
def respond():
    # retrieve the message in JSON and then transform it to a Telegram object
    update = telegram.Update.de_json(request.get_json(force=True), bot)

    if update.callback_query is None:
        if update.message.text is not None:
            # Telegram understands UTF-8, so encode text for unicode compatibility
            text = update.message.text.encode('utf-8').decode()
            chat_id = update.message.chat.id
            username = update.message.from_user.username
            message_id = update.message.message_id
            print("Text \"" + text + "\"" + " from " + username + " in chat_id " + str(chat_id))

            if text == commands["start"]:
                Sender.start_message(bot, chat_id)
            elif text == commands["keyboard"]:
                Sender.keyboard_message(bot, chat_id)
            elif text == commands["soundbite"]:
                Sender.soundbite_message(bot, chat_id)
            elif text == commands["image"]:
                Sender.image_message(bot, chat_id)
            elif text == commands["reply"]:
                Sender.reply_message(bot, chat_id, message_id)
            elif text.startswith(commands["echo_after"]):
                Sender.echo_after_message(bot, chat_id, message_id, text)
            elif text.startswith(commands["edit"]):
                Sender.edit_message(bot, chat_id, message_id, text)

        return '', 200
    else:
        Sender.reply_callback(bot, update.callback_query)
        return '', 200


@app.route('/set_webhook', methods=['GET', 'POST'])
def set_webhook():
    set_web_hook = bot.set_webhook(
        url='{URL}{HOOK}'.format(URL=URL, HOOK=bot_token),
        allowed_updates=[telegram.Update.CALLBACK_QUERY, telegram.Update.MESSAGE],
    )

    if set_web_hook:
        return "Webhook setup success"
    else:
        return "Webhook setup failed"


@app.route('/')
def index():
    return '.'


if __name__ == '__main__':
    app.run(threaded=True)
