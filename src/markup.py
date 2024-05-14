from aiogram.types import KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
import test_questions


def markup_test():
    kb = [
        [
            KeyboardButton(text='Первое'),
            KeyboardButton(text='Второе'),
        ],
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    return keyboard


# def markup_test_1():
#     kb = [
#         [
#             KeyboardButton(text=test_questions.q1a),
#         ],
#         [
#             KeyboardButton(text=test_questions.q1b),
#         ],
#     ]
#     keyboard = ReplyKeyboardMarkup(
#         keyboard=kb,
#         resize_keyboard=True,
#     )
#     return keyboard


# def markup_test_2():
#     kb = [
#         [
#             KeyboardButton(text=test_questions.q2a),
#         ],
#         [
#             KeyboardButton(text=test_questions.q2b),
#         ],
#     ]
#     keyboard = ReplyKeyboardMarkup(
#         keyboard=kb,
#         resize_keyboard=True,
#     )
#     return keyboard


# def markup_test_3():
#     kb = [
#         [
#             KeyboardButton(text=test_questions.q3a),
#         ],
#         [
#             KeyboardButton(text=test_questions.q3b),
#         ],
#     ]
#     keyboard = ReplyKeyboardMarkup(
#         keyboard=kb,
#         resize_keyboard=True,
#     )
#     return keyboard


# def markup_test_4():
#     kb = [
#         [
#             KeyboardButton(text=test_questions.q4a),
#         ],
#         [
#             KeyboardButton(text=test_questions.q4b),
#         ],
#     ]
#     keyboard = ReplyKeyboardMarkup(
#         keyboard=kb,
#         resize_keyboard=True,
#     )
#     return keyboard


# def markup_test_5():
#     kb = [
#         [
#             KeyboardButton(text=test_questions.q5a),
#         ],
#         [
#             KeyboardButton(text=test_questions.q5b),
#         ],
#     ]
#     keyboard = ReplyKeyboardMarkup(
#         keyboard=kb,
#         resize_keyboard=True,
#     )
#     return keyboard


# def markup_test_6():
#     kb = [
#         [
#             KeyboardButton(text=test_questions.q6a),
#         ],
#         [
#             KeyboardButton(text=test_questions.q6b),
#         ],
#     ]
#     keyboard = ReplyKeyboardMarkup(
#         keyboard=kb,
#         resize_keyboard=True,
#     )
#     return keyboard


# def markup_test_7():
#     kb = [
#         [
#             KeyboardButton(text=test_questions.q7a),
#         ],
#         [
#             KeyboardButton(text=test_questions.q7b),
#         ],
#     ]
#     keyboard = ReplyKeyboardMarkup(
#         keyboard=kb,
#         resize_keyboard=True,
#     )
#     return keyboard

# def markup_test_8():
#     kb = [
#         [
#             KeyboardButton(text=test_questions.q8a),
#         ],
#         [
#             KeyboardButton(text=test_questions.q8b),
#         ],
#     ]
#     keyboard = ReplyKeyboardMarkup(
#         keyboard=kb,
#         resize_keyboard=True,
#     )
#     return keyboard


# def markup_test_9():
#     kb = [
#         [
#             KeyboardButton(text=test_questions.q9a),
#         ],
#         [
#             KeyboardButton(text=test_questions.q9b),
#         ],
#     ]
#     keyboard = ReplyKeyboardMarkup(
#         keyboard=kb,
#         resize_keyboard=True,
#     )
#     return keyboard


# def markup_test_10():
#     kb = [
#         [
#             KeyboardButton(text=test_questions.q10a),
#         ],
#         [
#             KeyboardButton(text=test_questions.q10b),
#         ],
#     ]
#     keyboard = ReplyKeyboardMarkup(
#         keyboard=kb,
#         resize_keyboard=True,
#     )
#     return keyboard


# def markup_test_11():
#     kb = [
#         [
#             KeyboardButton(text=test_questions.q11a),
#         ],
#         [
#             KeyboardButton(text=test_questions.q11b),
#         ],
#     ]
#     keyboard = ReplyKeyboardMarkup(
#         keyboard=kb,
#         resize_keyboard=True,
#     )
#     return keyboard


# def markup_test_12():
#     kb = [
#         [
#             KeyboardButton(text=test_questions.q12a),
#         ],
#         [
#             KeyboardButton(text=test_questions.q12b),
#         ],
#     ]
#     keyboard = ReplyKeyboardMarkup(
#         keyboard=kb,
#         resize_keyboard=True,
#     )
#     return keyboard


# def markup_test_13():
#     kb = [
#         [
#             KeyboardButton(text=test_questions.q13a),
#         ],
#         [
#             KeyboardButton(text=test_questions.q13b),
#         ],
#     ]
#     keyboard = ReplyKeyboardMarkup(
#         keyboard=kb,
#         resize_keyboard=True,
#     )
#     return keyboard


# def markup_test_14():
#     kb = [
#         [
#             KeyboardButton(text=test_questions.q14a),
#         ],
#         [
#             KeyboardButton(text=test_questions.q14b),
#         ],
#     ]
#     keyboard = ReplyKeyboardMarkup(
#         keyboard=kb,
#         resize_keyboard=True,
#     )
#     return keyboard


# def markup_test_15():
#     kb = [
#         [
#             KeyboardButton(text=test_questions.q15a),
#         ],
#         [
#             KeyboardButton(text=test_questions.q15b),
#         ],
#     ]
#     keyboard = ReplyKeyboardMarkup(
#         keyboard=kb,
#         resize_keyboard=True,
#     )
#     return keyboard


# def markup_test_16():
#     kb = [
#         [
#             KeyboardButton(text=test_questions.q16a),
#         ],
#         [
#             KeyboardButton(text=test_questions.q16b),
#         ],
#     ]
#     keyboard = ReplyKeyboardMarkup(
#         keyboard=kb,
#         resize_keyboard=True,
#     )
#     return keyboard


# def markup_test_17():
#     kb = [
#         [
#             KeyboardButton(text=test_questions.q17a),
#         ],
#         [
#             KeyboardButton(text=test_questions.q17b),
#         ],
#     ]
#     keyboard = ReplyKeyboardMarkup(
#         keyboard=kb,
#         resize_keyboard=True,
#     )
#     return keyboard


# def markup_test_18():
#     kb = [
#         [
#             KeyboardButton(text=test_questions.q18a),
#         ],
#         [
#             KeyboardButton(text=test_questions.q18b),
#         ],
#     ]
#     keyboard = ReplyKeyboardMarkup(
#         keyboard=kb,
#         resize_keyboard=True,
#     )
#     return keyboard


# def markup_test_19():
#     kb = [
#         [
#             KeyboardButton(text=test_questions.q19a),
#         ],
#         [
#             KeyboardButton(text=test_questions.q19b),
#         ],
#     ]
#     keyboard = ReplyKeyboardMarkup(
#         keyboard=kb,
#         resize_keyboard=True,
#     )
#     return keyboard


# def markup_test_20():
#     kb = [
#         [
#             KeyboardButton(text=test_questions.q20a),
#         ],
#         [
#             KeyboardButton(text=test_questions.q20b),
#         ],
#     ]
#     keyboard = ReplyKeyboardMarkup(
#         keyboard=kb,
#         resize_keyboard=True,
#     )
#     return keyboard


def markup_main():
    kb = [
        [
            KeyboardButton(text='Пройти тест 📃'),
            KeyboardButton(text='Посмотреть результат 🖨️')
        ],
        [
            KeyboardButton(text='Выбрать предметы 📖'),
        ],
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    return keyboard


# def markup_subjects():
#     kb = [
#         [
#             KeyboardButton(text='Математика 📐'),
#             KeyboardButton(text='Русский 📗'),
#         ],
#         [
#             KeyboardButton(text='Информатика 💻'),
#             KeyboardButton(text='Физика 🛰️'),
#         ],
#         [
#             KeyboardButton(text='Химия 🥼'),
#             KeyboardButton(text='Биология 🩺'),
#         ],
#         [
#             KeyboardButton(text='История 🗳️'),
#             KeyboardButton(text='География 🌍'),
#         ],
#         [
#             KeyboardButton(text='Обществознание 🎓'),
#             KeyboardButton(text='Литература 📘'),
#         ],
#         [
#             KeyboardButton(text='Иностранный язык ㊗️'),
#         ],
#         [
#             KeyboardButton(text='Готово ✔️'),
#         ],
#     ]
#     keyboard = ReplyKeyboardMarkup(
#         keyboard=kb,
#         resize_keyboard=True,
#     )
#     return keyboard


def markup_subjects():
    kb = [
        [
            KeyboardButton(text='Математика'),
            KeyboardButton(text='Русский'),
        ],
        [
            KeyboardButton(text='Информатика'),
            KeyboardButton(text='Физика'),
        ],
        [
            KeyboardButton(text='Химия'),
            KeyboardButton(text='Биология'),
        ],
        [
            KeyboardButton(text='История'),
            KeyboardButton(text='География'),
        ],
        [
            KeyboardButton(text='Обществознание'),
            KeyboardButton(text='Литература'),
        ],
        [
            KeyboardButton(text='Иностранный язык'),
        ],
        [
            KeyboardButton(text='Готово'),
        ],
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
