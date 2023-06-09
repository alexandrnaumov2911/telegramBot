import os

from aiogram import types

ADMINS = (747184261,)
TOKEN = os.getenv('TOKEN')
NGROK = os.getenv('NGROK', '')

WEBHOOK_PATH = ''
WEBHOOK_URL = f'{NGROK}{WEBHOOK_PATH}'


WEBAPP_HOST = '127.0.0.1'  # or ip
WEBAPP_PORT = 8000

if not TOKEN:
    exit('Error: no token provided')

COMMANDS = [
    types.BotCommand('start', 'Стартуем!'),
    types.BotCommand('about', 'О себе'),
    types.BotCommand('block', 'Для проверки чс, (/block ~user_id~ ~причина~)'),
    types.BotCommand('feedback', 'Оставить отзыв'),
    types.BotCommand('location', 'Отправить локацию'),
    types.BotCommand('favorite_film', 'Мой любимый фильм'),
    types.BotCommand('multi_menu', 'Перейти в меню'),
    types.BotCommand('start_polling', 'Опрос по любимому жанру фильмов'),
]

