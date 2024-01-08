from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.core.models.base import Base
from src.core.models.mixins import UserRelationMixin


class Profile(UserRelationMixin, Base):
    _user_id_unique = True
    _user_back_populates = "profile"
    first_name: Mapped[str | None] = mapped_column(String(40), unique=False)
    last_name: Mapped[str | None] = mapped_column(String(40), unique=False)
    bio: Mapped[str | None]
