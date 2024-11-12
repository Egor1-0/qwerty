from sqlalchemy import select

from app.database.models import User, Card
from app.database.session import async_session

async def get_user_by_tg_id(tg_id: int) -> User | None:
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        return user
    

async def get_guest_card(phone: str) -> str:
    async with async_session() as session:
        card = await session.scalar(select(Card).where(Card.phone == phone))
        return card