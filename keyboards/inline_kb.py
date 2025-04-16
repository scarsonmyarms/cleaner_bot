from aiogram.types import (InlineKeyboardMarkup, #Этот класс используется для создания разметки инлайн клавиатуры. Разметка определяет, как будут располагаться кнопки на клавиатуре и как они будут взаимодействовать с пользователем.
                           InlineKeyboardButton, #Этот класс представляет собой отдельную кнопку на инлайн клавиатуре. С помощью него мы можем задавать текст кнопки и действие, которое произойдет при нажатии на неё, например, отправку CallBack данных
                           WebAppInfo) #Этот класс используется для создания кнопок, которые открывают веб-приложения внутри Telegram. С его помощью можно определить URL веб-приложения, которое будет открыто при нажатии на кнопку.
from aiogram.utils.keyboard import InlineKeyboardBuilder #Это удобный инструмент для построения инлайн клавиатур. С его помощью можно легко и быстро создавать клавиатуры, добавляя кнопки и определяя их расположение
from create_bot import admins

def admin_kb(user_telegram_id: int):
    kb_list = [
        [InlineKeyboardButton(text='popa', callback_data='add_job')]
    ]
    if user_telegram_id == admins:
        kb_list.append([InlineKeyboardButton(text='створити роботу', callback_data='add_job')])
        kb_list.append([InlineKeyboardButton(text='stat worler', callback_data='worker stat')])

    return InlineKeyboardMarkup(inline_keyboard=kb_list)

#Инлайн-клавиатура проверки заполнения данных
def check_data():
    kb_list = [
        [InlineKeyboardButton(text="✅Все верно", callback_data='correct')],
        [InlineKeyboardButton(text="❌Заполнить сначала", callback_data='incorrect')]
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=kb_list)
    return keyboard
