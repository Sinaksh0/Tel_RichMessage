from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from database import load_users
from src.send_richmessage import send_rich_message
from keyboards.inlinekeyboard import main_keyboard, admin_keyboard
from src.text import WELCOME, HTML, MEDIA
from src.api import ADMIN_ID

async def callback_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    message_id = query.message.message_id
    chat = update.effective_chat
    person = update.effective_user

    if context.user_data['chat_id']:
        chat_id = context.user_data['chat_id']
    else:
        chat_id = chat.id

    data = query.data

    await query.answer()

    back = [
            [InlineKeyboardButton('🔙 بازگشت', callback_data='back')]
        ]
    keyboard = InlineKeyboardMarkup(back).to_dict()

    if data == 'html':
        await send_rich_message(chat_id, HTML, 'editMessageText', keyboard, message_id)

    elif data == 'media':
        await send_rich_message(chat_id, MEDIA, 'editMessageText', keyboard, message_id)

    elif data == 'right':
        if not context.user_data['rich_html']:
            return
        await send_rich_message(chat_id, context.user_data['rich_html'], 'sendRichMessage', rtl=True)

    elif data == 'left':
        if not context.user_data['rich_html']:
            return
        await send_rich_message(chat_id, context.user_data['rich_html'], 'sendRichMessage', rtl=False)

    elif data == 'members':
        users = load_users()
        count = len(users)

        message = f"<h2>👥 کاربران ثبت‌ شده: {count}</h2>"
        message += "<p><strong>📋 فهرست کاربران</strong></p>"

        for user in users:
            message += f"<ul><li>{user['Name']} | <code>{user['ID']}</code></li></ul>"

        await send_rich_message(chat_id, message, 'editMessageText', keyboard, message_id, False)

    elif data == 'back':
        if chat.type == 'private' and person.id == ADMIN_ID:
            main = admin_keyboard()
        else:
            main = main_keyboard()

        await send_rich_message(chat_id, WELCOME, 'editMessageText', main, message_id)
