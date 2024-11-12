from sqlalchemy import select, update

from app.database.models import User
from app.database.session import async_session


async def update_user_phone(tg_id: int, phone: str) -> None:
    async with async_session() as session:
        await session.execute(update(User).where(User.tg_id == tg_id)
                              .values(phone=phone))
        await session.commit()