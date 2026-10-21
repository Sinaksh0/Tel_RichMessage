from telegram import InlineKeyboardMarkup, InlineKeyboardButton

def main_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton(text="🌐 راهنمای HTML", callback_data="html"),
            InlineKeyboardButton(text="🖼 راهنمای مدیا", callback_data="media")
        ],
    ]

    markup = InlineKeyboardMarkup(keyboard).to_dict()
    return markup

def admin_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton(text="🌐 راهنمای HTML", callback_data="html"),
            InlineKeyboardButton(text="🖼 راهنمای مدیا", callback_data="media")
        ],
        [InlineKeyboardButton(text="📊 لیست کاربران", callback_data="members")]
    ]

    markup = InlineKeyboardMarkup(keyboard).to_dict()
    return markup

def rtl() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton(text="راست چین", callback_data="right"),
            InlineKeyboardButton(text="چپ چین", callback_data="left")
        ]
    ]

    return InlineKeyboardMarkup(keyboard)
