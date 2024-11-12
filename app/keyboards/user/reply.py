from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

phone_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Отправить номер', request_contact=True)]
], resize_keyboard=True)

delete_kb = ReplyKeyboardRemove()