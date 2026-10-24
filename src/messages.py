from telegram import Update, MessageOriginChannel
from telegram.ext import ContextTypes
from src.api import ADMIN_ID
from src.text import WELCOME
from keyboards.inlinekeyboard import main_keyboard, admin_keyboard, rtl
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
        name = chat.title if chat.title else 'Super Group'
    else:
        name = user.full_name if user.full_name else 'Super Group'

    check_user(name, chat_id)

    await context.bot.set_message_reaction(chat_id=update.message.chat_id,
        message_id=update.message.message_id,
        reaction=['\U0001f60d']
    )

    await send_rich_message(chat_id, WELCOME, 'sendRichMessage', keyboard)
    return

async def send_to_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    await context.bot.set_message_reaction(chat_id=update.message.chat_id,
        message_id=update.message.message_id,
        reaction=['\U0001f44d']
    )

    rest = text[len('/send'):].strip()
    if not rest:
        await update.message.reply_text('👤 گیرنده‌ی پیام رو مشخص کن. نمونه:\n/manager all سلام\n/manager 123456789 سلام')
        return

    target = rest.split()[0]
    msg = ' '.join(rest.split()[1:]).strip()

    if not msg:
        await update.message.reply_text('✍️ متن پیام رو هم بنویس. نمونه:\n/manager all سلام\n/manager 123456789 سلام')
        return

    if target.lower() == 'all':
        users = load_users()
        sent = 0
        failed = 0
        for user in users:
            chat_id = user.get('ID')
            if chat_id is None:
                continue
            try:
                await context.bot.send_message(chat_id=chat_id, text=f'📨 پیام از مدیر برای شما\n\n{msg}')
                sent += 1
            except Exception:
                failed += 1
        await update.message.reply_text(f'📨 ارسال همگانی انجام شد؛ {sent} پیام موفق بود.' + (f' ⚠️ {failed} پیام ارسال نشد.' if failed else ' ✅'))
        return

    elif target.isdigit() or (target.startswith('-') and target[1:].isdigit()):
        try:
            chat_id = int(target)
            await context.bot.send_message(chat_id=chat_id, text=f'📨 پیام از مدیر برای شما\n\n{msg}')
            await update.message.reply_text(f'✅ پیام با موفقیت به آیدی {chat_id} رسید.')
        except Exception as exc:
            await update.message.reply_text(f'❌ ارسال پیام به آیدی {target} ناموفق بود.\nجزئیات: {exc}')
        return
        
    else:
        await update.message.reply_text('⚠️ گیرنده رو با «all» یا یک آیدی عددی مشخص کن.\nنمونه: /manager all سلام')
    
async def message_hadler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texts = update.message

    if texts.forward_origin and isinstance(texts.forward_origin, MessageOriginChannel):
        origin = texts.forward_origin
        username = f"@{origin.chat.username}" if origin.chat.username else "ندارد (خصوصی)"
        title = origin.chat.title or "بدون نام"

        await texts.reply_text(
            f"📢 اطلاعات پیام فورواردشده از کانال\n\n"
            f"📌 نام کانال: {title}\n"
            f"🆔 آیدی کانال: <code>{origin.chat.id}</code>\n"
            f"🔗 یوزرنیم: {username}\n"
            f"🔢 آیدی پیام در کانال: {origin.message_id}",
            parse_mode='HTML'
        )
        return

    message = texts.text
    if not message:
        return

    try:
        chat_id = int(message.split()[0])
    except ValueError:
        pass
    
    text = ' '.join(message.split()[1:]).strip()

    if text.startswith('<'):
        await context.bot.set_message_reaction(chat_id=update.message.chat_id,
            message_id=update.message.message_id,
            reaction=['\U0001f44d']
        )

        if chat_id:
            context.user_data['chat_id'] = chat_id

        context.user_data['rich_html'] = text
        markup = rtl()
        await update.message.reply_text('خروجی راست چین باشد یا خیر؟\nانتخاب کنید:', reply_markup=markup)

    return
