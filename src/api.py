import os

BOT_TOKEN = os.getenv('Bot_Token')
TELEGRAM_API = f'https://api.telegram.org/bot{BOT_TOKEN}'
GIT = os.getenv('Git')
KEY = os.getenv('Key')
ADMIN_ID = int(os.getenv('Admin'))
WEBHOOK = os.getenv('Webhook')
PORT = int(os.environ.get('PORT', 10000))
