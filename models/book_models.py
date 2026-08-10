from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Float, Integer

from database import Base


class BookModel(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
        autoincrement=True
    )

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    author: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    price: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    quantity: Mapped[int] = mapped_column(
        Integer,
        default=0
    )