import pathlib
from .Constants import commands
from telegram.constants import PARSEMODE_MARKDOWN
from telegram.inline.inlinekeyboardmarkup import InlineKeyboardMarkup
from telegram.inline.inlinekeyboardbutton import InlineKeyboardButton


def start_message(bot, chat_id):
    bot.sendMessage(
        chat_id=chat_id,
        text="This is an example message sent using /start",
    )

    return


def soundbite_message(bot, chat_id):
    sound_dir = str(pathlib.Path(__file__).parent.resolve()) + "/soundbites/"

    with open(sound_dir + 'Example.ogg', 'rb') as audio:
        bot.send_voice(chat_id=chat_id, voice=audio)
    return


def image_message(bot, chat_id):
    img_dir = str(pathlib.Path(__file__).parent.resolve()) + "/images/"
    caption = "This is an example of a caption"
    with open(img_dir + "Example.png", "rb") as image:
        bot.sendPhoto(chat_id=chat_id, photo=image,
                      caption=caption)

    return


def reply_message(bot, chat_id, message_id):
    bot.sendMessage(chat_id=chat_id,
                    text="This replies to your message",
                    reply_to_message_id=message_id)
    return


def edit_message(bot, chat_id, message_id, text):
    cmd = text.split("", 2)
    if len(cmd) != 3:
        bot.sendMessage(chat_id=chat_id,
                        text="Usage:\n /edit id new text\n Example: /edit 1 hello!",
                        reply_to_message_id=message_id)

    edit_message_id = cmd[1]
    edit_text = cmd[2]
    bot.edit_message_text(chat_id=chat_id, message_id=edit_message_id, text=edit_text)
    return


def echo_after_message(bot, chat_id, message_id, text):
    cmd = text.split()
    if cmd[0] != commands["echo_after"]:
        return 'ok'
    if len(cmd) < 2:
        bot.sendMessage(chat_id=chat_id,
                        text="Please add something after /echo_after for me to echo",
                        reply_to_message_id=message_id)
    else:
        msg = cmd[1].strip("", 1)
        bot.sendMessage(chat_id=chat_id, text=msg, reply_to_message_id=message_id)
    return


def keyboard_message(bot, chat_id):
    keyboard = [
        [
            InlineKeyboardButton("Option 1", callback_data='1'),
            InlineKeyboardButton("Option 2", callback_data='2'),
        ],
        [InlineKeyboardButton("Option 3", callback_data='3')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    bot.sendMessage(chat_id=chat_id, text="Please choose", reply_markup=reply_markup,
                    parse_mode=PARSEMODE_MARKDOWN)

    return


def reply_callback(bot, callback_query):
    callback_id = callback_query.id
    chat_id = callback_query.message.chat.id
    message_id = callback_query.message.message_id
    username = callback_query.from_user.username
    callback_msg = callback_query.message.text
    callback_data = callback_query.data

    bot.answerCallbackQuery(callback_id, "Button selected: " + callback_data)

    return
