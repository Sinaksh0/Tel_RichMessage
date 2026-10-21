from telegram import Update
from telegram.ext import ContextTypes
from src.api import ADMIN_ID
from src.text import WELCOME
from keyboards.inlinekeyboard import main_keyboard, admin_keyboard
from database import upload_github, load_users
from src.send_richmessage import send_rich_message

def check_user(name: str, chat_id: int):
    users = load_users()
    flag = True
    for id in users:
        if chat_id == id['ID']:
            flag = False
            break
        
    if flag:
        users.append({
            "Name": name,
            "ID": chat_id
        })
        upload_github(users)
        return

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    user = update.effective_user
    chat_id = chat.id

    if chat.type == 'private' and user.id == ADMIN_ID:
        keyboard = admin_keyboard()
    else:
        keyboard = main_keyboard()

    if chat.type in ['group', 'supergroup']:
        name = chat.title
    else:
        name = user.full_name

    check_user(name, chat_id)

    await context.bot.set_message_reaction(chat_id=update.message.chat_id,
        message_id=update.message.message_id,
        reaction=['\U0001f60d']
    )

    await send_rich_message(chat_id, WELCOME, 'sendRichMessage', keyboard)
    return

async def message_hadler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if not text:
        return

    await context.bot.set_message_reaction(chat_id=update.message.chat_id,
        message_id=update.message.message_id,
        reaction=['\U0001f44d']
    )
    
    if text.startswith('<'):
        await send_rich_message(update.effective_chat.id, text, 'sendRichMessage')

    return
