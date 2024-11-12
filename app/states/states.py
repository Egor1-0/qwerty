from aiogram.fsm.state import State, StatesGroup

class GetPhone(StatesGroup):
    phone = State()