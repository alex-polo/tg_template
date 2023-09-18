from typing import List

from sqlalchemy import String, Integer, TIMESTAMP, func
from sqlalchemy.orm import Mapped, mapped_column

# from sqlalchemy import mapped_column, Mapped

from database.lib import Base
from database.models.user_roles import UserRoles


class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    identifier: Mapped[int] = mapped_column(Integer, unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), unique=True, nullable=True)
    nickname: Mapped[str] = mapped_column(String(50), unique=True, nullable=True)
    phone_number: Mapped[str] = mapped_column(String(50), nullable=True)

    roles: Mapped[List[UserRoles]]

    create_on: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP, default=func.now, nullable=False)
    update_on: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP, default=func.now, onupdate=func.now, nullable=False)
