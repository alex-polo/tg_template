from sqlalchemy.orm import mapped_column, Mapped

from database.lib import Base


class UserRoles(Base):
    __tablename__ = 'user_roles'

    id: Mapped[int] = mapped_column(primary_key=True)
