from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from src.core.models.base import Base
from src.core.models.mixins import UserRelationMixin


class Post(UserRelationMixin, Base):
    _user_id_nullable = False
    _user_id_unique = False
    _user_back_populates = "posts"
    title: Mapped[str] = mapped_column(String(100))
    body: Mapped[str] = mapped_column(Text, default="", server_default="")
