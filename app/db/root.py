from .session import Base

from sqlalchemy import Column, Integer


class Root(Base):
    __tablename__ = "root"
    id = Column(Integer, primary_key=True)
