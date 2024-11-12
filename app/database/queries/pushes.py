from sqlalchemy import select

from app.database.session import async_session
from app.database.models import User

async def push_user(tg_id: int):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        if user: return
        user = User(tg_id=tg_id)
        session.add(user)
        await session.commit()