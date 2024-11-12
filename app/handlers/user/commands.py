from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from app.keyboards.user.inline import start_kb, get_info_about_card
from app.keyboards.user.reply import phone_kb, delete_kb
from app.database.queries import *
from app.states.states import *
from app.img import *
from app.const import *

user_commands_router = Router()


@user_commands_router.message(CommandStart())
async def cmd_start(message: Message):
    await push_user(message.from_user.id)
    user = await get_user_by_tg_id(message.from_user.id)
    await message.answer('Необходимый текст', reply_markup=start_kb(user.isAdmin))


@user_commands_router.callback_query(F.data == 'contacts')
async def cmd_contacts(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(contacts)


@user_commands_router.callback_query(F.data == 'guest_card')
async def cmd_bar_map(callback: CallbackQuery):
    await callback.answer()
    user = await get_user_by_tg_id(callback.from_user.id)
    if not user.phone:
        await callback.message.answer('Введите номер телефона', reply_markup=phone_kb)
        return

    card = await get_guest_card(user.phone)

    if not card:
        await callback.message.answer('У вас нет карты', reply_markup=get_info_about_card)
        return
    
    text = black_card if card.card == 'black' else gold_card
    photo = black_card_img if card.card == 'black' else gold_card_img
    await callback.message.answer_photo(photo, caption=text)
    


@user_commands_router.message(F.contact)
async def get_phone(message: Message):
    await update_user_phone(message.from_user.id, message.contact.phone_number)
    await message.answer('Номер телефона сохранен, попробуйте снова', reply_markup=delete_kb)