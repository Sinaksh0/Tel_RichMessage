from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters
from telegram import BotCommand
from src.api import BOT_TOKEN, WEBHOOK, PORT
from src.messages import start, send_to_user, message_hadler
from keyboards.callback import callback_handler

async def post_init(application):
    await application.bot.set_my_commands([
        BotCommand('start', '🚀 شروع و نمایش منو')
    ])

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.post_init = post_init

    
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('send', send_to_user))
    app.add_handler(MessageHandler(filters.FORWARDED | (filters.TEXT & ~filters.COMMAND), message_hadler))
    app.add_handler(CallbackQueryHandler(callback_handler))

    print('Bot is running...')
    app.run_webhook('0.0.0.0', PORT, "webhook", webhook_url=f"{WEBHOOK.rstrip('/')}/webhook")
