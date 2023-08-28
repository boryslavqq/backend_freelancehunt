from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


async def start_button() -> ReplyKeyboardMarkup:
    keyboard = [
        [
            KeyboardButton(text="HI!")
        ]
    ]

    kb = ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
    return kb
