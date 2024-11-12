from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def start_kb(isAdmin: bool) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.button(text='Крейзи-меню', callback_data='menu')
    builder.button(text='Карта бара', callback_data='bar_map')
    builder.button(text='Контакты', callback_data='contacts')
    builder.button(text='Забронировать стол', callback_data='booking_table')
    builder.button(text='Карта постоянного гостя', callback_data='guest_card')
    
    if isAdmin:
        builder.button(text='Админ-панель', callback_data='admin_panel')

    builder.adjust(2)

    return builder.as_markup()

get_info_about_card = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Получить информацию о карте', url='https://google.com')]
], resize_keyboard=True)