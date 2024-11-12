from enum import Enum

from sqlalchemy import String, BigInteger
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base

class CardType(str, Enum):
    black = 'black'
    gold = 'gold'



class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id: Mapped[int] = mapped_column(BigInteger)
    phone: Mapped[str] = mapped_column(String, nullable=True)
    isAdmin: Mapped[bool] = mapped_column(default=False)


class Card(Base):
    __tablename__ = 'cards'

    id: Mapped[int] = mapped_column(primary_key=True)
    phone: Mapped[int] = mapped_column(String)
    card: Mapped[CardType]