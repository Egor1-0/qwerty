from aiogram import Router

from app.handlers.user.commands import user_commands_router

user_router = Router()
user_router.include_routers(user_commands_router)