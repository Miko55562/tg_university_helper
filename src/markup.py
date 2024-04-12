from aiogram.types import KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup


def markup_main():
    kb = [
        [
            KeyboardButton(text='Пройти тест'),
            KeyboardButton(text='Посмотреть результат')
        ],
        # [
        #     KeyboardButton(text='График'),
        #     KeyboardButton(text='Настройки')
        # ],
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    return keyboard


def markup_cancle():
    kb = [
        [
            KeyboardButton(text='Назад'),
        ],
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    return keyboard
