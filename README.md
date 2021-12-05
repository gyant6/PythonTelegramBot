# PythonTelegramBot
Clone this repository to get a quickstart on your own Telegram Bot in Python 3.9

## Setting up the project
1. Use ```source venv/bin/activate``` in the project root to use a virtual environment

2. ```pip install package_name``` to install missing packages. For this project, the following packages are needed
   - ```pip install python-telegram-bot```
   - ```pip install gunicorn```
   - ```pip install flask```

The rest of this guide assumes you are using Heroku to deploy your bot. 

## Creating your Telegram Bot
Message https://t.me/BotFather to create your own bot. 
1. Use /newbot to start the process
2. Give your bot a unique username
3. Receive your bot token. It looks something like this
   - ```0123456789:AAaaAAaa0aAA0aaaAaAAAa0aaa0aa_00AAA```
   
## Setting up the bot in Heroku
1. In Heroku Dashboard, go to https://dashboard.heroku.com/apps/your-python-telegram-bot/settings and set the following environment variables. 
This is necessary so we do not publish our private token anywhere on the web.

Key | Value
--- | --- 
bot_token | 0123456789:AAaaAAaa0aAA0aaaAaAAAa0aaa0aa_00AAA
URL | https://your-python-telegram-bot.herokuapp.com [^1]

2. Push your code to Heroku
3. Go to https://your-python-telegram-bot.herokuapp.com/set_webhook [^1] to allow your bot to receive messages

## Adding new features
1. If you add new imports, remember to do ```pip freeze > requirements.txt```.
This updates the ```requirements.txt``` file to let Heroku know what packages needs to be installed. Push the new file as well.

[^1]: Replace with your own url
