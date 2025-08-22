from ..session import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String


class UserData(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(50), nullable=False, unique=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    rights: Mapped[str] = mapped_column(String(20), nullable=False, default="user")
    email: Mapped[str] = mapped_column(String(100), nullable=False, unique=True, index=True)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)  # храним только хэш

    def __repr__(self) -> str:
        return f"<UserData id={self.id} username={self.username} email={self.email}>"
