import logging
import asyncio

from aiogram import Bot, Dispatcher

from app.database.session import create_session
from app.handlers.user import user_router
from config import TOKEN

async def main():
    await create_session()
    bot = Bot(token=TOKEN) 
    dp = Dispatcher()

    dp.include_routers(user_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass