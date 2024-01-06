from sqlalchemy.orm import Mapped

from src.core.models.base import Base


class Product(Base):
    name: Mapped[str]
    description: Mapped[str]
    price: Mapped[int]
